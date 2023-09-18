---
title: langchain-streamlit-demo
emoji: 🦜
colorFrom: green
colorTo: red
sdk: docker
app_port: 7860
pinned: true
tags: [langchain, streamlit, docker]
---

# langchain-streamlit-demo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?&logo=docker&logoColor=white)](https://hub.docker.com/r/joshuasundance/langchain-streamlit-demo)
[![Docker Image Size (tag)](https://img.shields.io/docker/image-size/joshuasundance/langchain-streamlit-demo/latest)](https://hub.docker.com/r/joshuasundance/langchain-streamlit-demo)
[![Open HuggingFace Space](https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/joshuasundance/langchain-streamlit-demo)


This project shows how to build a simple chatbot UI with [Streamlit](https://streamlit.io) and [LangChain](https://langchain.com).

This `README` was written by [Claude 2](https://www.anthropic.com/index/claude-2), an LLM from [Anthropic](https://www.anthropic.com/).

# Features
- Chat interface for talking to AI assistant
- Streaming output of assistant responses
- Leverages LangChain for dialogue management
- Integrates with [LangSmith](https://smith.langchain.com) for tracing conversations
- Allows giving feedback on assistant's responses

# Usage
## With Docker (pull from Docker Hub)
1. Run in terminal: `docker run -p 7860:7860 joshuasundance/langchain-streamlit-demo:latest`
2. Open http://localhost:7860 in your browser.

## Docker Compose
1. Clone the repo. Navigate to cloned repo directory.
2. Run in terminal: `docker-compose up`
3. Then open http://localhost:7860 in your browser.

# Configuration
- Enter your OpenAI API key to power the assistant
- Optionally enter a LangSmith API key to enable conversation tracing
- Customize the assistant prompt and temperature

# Code Overview
- `app.py` - Main Streamlit app definition
- `llm_stuff.py` - LangChain helper functions

# Deployment
The app is packaged as a Docker image for easy deployment. It is published to Docker Hub and Hugging Face Spaces:

- [DockerHub](https://hub.docker.com/r/joshuasundance/langchain-streamlit-demo)
- [HuggingFace Spaces](https://huggingface.co/spaces/joshuasundance/langchain-streamlit-demo)

CI workflows in `.github/workflows` handle building and publishing the image.

# Links
- [Streamlit](https://streamlit.io)
- [LangChain](https://langchain.com)
- [LangSmith](https://smith.langchain.com)

# TODO
1. Let user choose between `gpt-3.5-turbo` and `gpt-4`
2. Add support for Anthropic and Anyscale chat models
3. More customization / parameterization in sidebar
