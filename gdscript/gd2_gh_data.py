from tqdm import tqdm
import requests
import pandas as pd
import base64
from datasets import Dataset
from git import Repo
import os

access_token = "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"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer " + access_token,
    "X-GitHub-Api-Version": "2022-11-28",
}

page = 1
per_page = 100
#query = 'config/features=PackedStringArray(\"4.0\")&per_page={p}&page={page}'
# Define the GitHub API endpoint for repository search
url = 'https://api.github.com/search/code?q=config/features=PackedStringArray(\"4.0\")&per_page={per_page}&page={page}'

def process_repositories(repo_urls):
    
    
    for repo in tqdm(repo_urls, desc=f"processing repos"):
        print(f"Processing repository: {repo}")
        
        # Clone the repository to the local file system
        repo_path = f"repos/{repo[1]}"
        repo_url = repo[0]
        repo_name = repo[1]
        Repo.clone_from(repo_url, repo_path, env={"GIT_TERMINAL_PROMPT": "0"}, progress=None)

        # Read the contents of .gd files
        for root, dirs, files in os.walk(repo_path):
            for file in tqdm(files):
                if file.endswith(".gd"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        try:
                            file_contents = f.read()

                            # Calculate line statistics
                            lines = file_contents.split("\n")
                            line_lengths = [len(line) for line in lines if line.strip()]
                            avg_line_length = sum(line_lengths) / len(line_lengths) if line_lengths else 0
                            max_line_length = max(line_lengths) if line_lengths else 0

                            # Calculate alphanumerical fraction
                            alphanum_chars = sum(c.isalnum() for c in file_contents)
                            alphanum_fraction = alphanum_chars / len(file_contents) if len(file_contents) > 0 else 0             

                            file_details.append({
                                "content": file_contents,
                                "avg_line_length": avg_line_length,
                                "max_line_length": max_line_length,
                                "alphanum_fraction": alphanum_fraction,
                            })
                        except:
                            # just skip the file if we encounter problems while reading it.
                            continue

        # Delete the repository from the file system
        os.system(f"rm -rf {repo_path}")

        print(f"Repository {repo_name} processed and deleted.\n")

# Create an empty list to store the file details
file_details = []
repo_urls = set()

# Send the initial request to the API and get the response
print("Fetching page 1")
response = requests.get(url.format(per_page=per_page, page=page), headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON data from the response
    data = response.json()
    # Extract the total number of repositories
    total_repos = data["total_count"]
    # Extract the list of repository trees from the data
    repositories = data["items"]
    repos_urls = {
        (r["repository"]["html_url"],r["repository"]["name"]) for r in repositories
    }

    # Handle pagination for more than 100 repositories
    remaining_repos = total_repos - per_page
    page = 2
    while remaining_repos > 0:
        
        print(f"Fetching page {page}")
        response = requests.get(url.format(per_page=per_page,page=page), headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            repositories = data["items"]
            
            # continue to collect the repo ids for processing later
            repo_urls = repo_urls.union({(r["repository"]["html_url"],r["repository"]["name"]) for r in repositories})
            
            remaining_repos -= per_page
            page += 1

        else:
            print("Error: Could not retrieve repositories.")
            break
    
    # process the repo trees
    process_repositories(repo_urls)
    # Convert the file details list into a DataFrame
    df = pd.DataFrame(file_details)
    print(df)
    
    df.to_parquet('gdscript2.parquet')
    
    # Define the dataset schema
    schema = {
        'content': str,
        'size': int,
        'lang': str,
        'ext': str,
        'avg_line_length': float,
        'max_line_length': int,
        'alphanum_fraction': float,
        'hexsha': str
    }

    print("Data saved as 'gdscript2.parquet'")
    print("---------------------------------------")
else:
    # Print an error message if the request was not successful
    print("Error: Could not retrieve repositories.")
