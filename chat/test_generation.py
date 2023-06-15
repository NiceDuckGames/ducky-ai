import argparse
import torch
from dialogues import DialogueTemplate, get_dialogue_template
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, set_seed

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_id",
        type=str,
        help="Name of model to generate samples with",
    )
    parser.add_argument(
        "--revision",
        type=str,
        default=None,
        help="The model repo's revision to use",
    )
    parser.add_argument(
        "--system_prompt", type=str, default=None, help="Overrides the dialogue template's system prompt"
    )
    args = parser.parse_args()
    
    dialogue_template = DialogueTemplate.from_pretrained(args.model_id, revision=args.revision)
    # tokenizer = AutoTokenizer.from_pretrained(args.model_id, revision=args.revision)
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_id,
        revision=args.revision,
        trust_remote_code=True,
    )
    
    generation_config = GenerationConfig(
        temperature=0.2,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.convert_tokens_to_ids(dialogue_template.end_token),
        min_new_tokens=32,
        max_new_tokens=256,
    )
    
    # model = AutoModelForCausalLM.from_pretrained(
    #     args.model_id,
    #     device_map="auto",
    #     revision=args.revision,
    #     torch_dtype=torch.float16,
    #     trust_remote_code=True,
    #     use_cache=False,
    # )
    # model.resize_token_embeddings(len(tokenizer))
    
    model = AutoModelForCausalLM.from_pretrained(
        args.model_id, revision=args.revision, load_in_8bit=True, trust_remote_code=True, device_map="auto", torch_dtype=torch.float16
    )

    inputs = tokenizer(
        "<|system|>\n<|end|>\n<|user|>\nWrite a function to validate an email address in JavaScript<|end|>\n<|assistant|>",
        return_tensors="pt",
        return_token_type_ids=False,
    ).to("cuda:0")
    
    print(inputs)
    outputs = model.generate(
        inputs=inputs,
    )
    print(f"=== EXAMPLE {idx} ===")
    print()
    print(tokenizer.decode(outputs[0], skip_special_tokens=False))
    print()
    print("======================")
    print()

if __name__ == "__main__":
    main()