# Ducky-AI
Ducky is LLM (large language model) project which aims to bring the power of AI to the game creation process within Godot.
Ducky is trained on open-source data that allows it to serve as a helpful game design assistant and it's even capable of using the Godot game engine itself based on simple English prompting!

# How to use this repository

## Quick Start

### Installation

- install pypyr
- install llm-foundry deps
```
cd llm-foundry
pip install -e ".[gpu]"
```

### Running finetuneing tasks

### Changing the seed model

*seed model is the model that is used within the first finetuning task that is ran. The subsequent tasks will likely use the resulting checkpoints of the previous finetuning task*

## Structure
This project is built around Mosaic ML's fantastic [llm-foundry](https://github.com/mosaicml/llm-foundry) project.

```
.
├── finetune
│   ├── chat
│   ├── godot4_docs
│   ├── godot_recorder
│   └── tscn_gdscript2
└── llm-foundry
```

Each finetuning task lives in it's own folder under the `finetune` directory. 
A finetuning task typically consists of a YAML file which is used with llm-foundry to do the training.
You may also find additional data collection and data pre-processing scripts inside any given finetuning directory.

At the root of the project you will find another YAML file which is used with the tool Pypyr. This is used to allow for easy orchestration of finetuning jobs.

# Adding a new finetuning task

*TODO: write this section :)*