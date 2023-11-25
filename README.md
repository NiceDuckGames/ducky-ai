# Ducky AI 

![Project Logo](./logo.png)

## Overview

This project is a game design assistant written in Rust that utilizes Large Language Models (LLMs) for Retrieval-Augmented Generation (RAG) based inferencing. It is designed to assist game developers in generating creative ideas and content for their games. The project is built with the Godot Game Engine integration in mind, as such the LLM is capable of carrying out actions for the user in the engine, using a custome developed engine command syntax.

## Features

- **Rust Implementation:** The core functionality is implemented in Rust, taking advantage of the language's performance and safety features.

- **LLMs for RAG Inference:** The application leverages state-of-the-art Large Language Models to perform Retrieval-Augmented Generation (RAG), enabling it to generate creative and contextually relevant suggestions for game design elements.

- **Godot Game Engine Integration:** Designed to seamlessly integrate with the Godot Game Engine, providing an efficient workflow for game developers.

## Getting Started

### Prerequisites

- Rust (version >= 1.54)
- Godot Game Engine (version >= 4.0)

### Building the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/game-design-assistant.git
   ```

2. Build the Rust application:

   ```bash
   cd game-design-assistant
   cargo build --release
   ```

### Running the plugin for remote inference against duckyai.niceduck.games

**TODO**

### Running the Application for local inference

**TODO**


## Usage

**TODO**

## Contributing

**TODO**

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The project relies on the incredible work of the open-source Rust and Godot communities.
- The LLM models used are powered by [Hugging Face Transformers](https://huggingface.co/transformers/).
- A big thanks to the [Candle project](https://github.com/huggingface/candle) and [Qdrant](https://github.com/qdrant/qdrant).

---

Feel free to customize this template according to the specific details of your project. Include additional sections such as installation instructions, troubleshooting, and any other relevant information for users and contributors.