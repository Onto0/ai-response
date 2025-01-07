# Discord Typing Bot (GPT-2 Powered)

This is a Python script that generates and types messages in Discord (or any text field) using GPT-2 from Hugging Face. The script simulates typing by automating keyboard inputs with the `pynput` library.

## Features
- Generates random story continuations using GPT-2.
- Simulates realistic typing in Discord or other chat applications.
- Automatically sends messages by simulating the Enter key.

---

## How It Works
1. **GPT-2 Model**: The script uses the `transformers` library to load the GPT-2 model.
2. **Keyboard Simulation**: The `pynput` library is used to simulate typing and pressing the Enter key.
3. **Story Generation**: A user provides a starting sentence, and the model generates the next parts of the story.
4. **Automated Typing**: The generated response is typed out character by character with adjustable speed.

---

## Installation
### Prerequisites
- Python 3.8+
- `transformers` (by Hugging Face)
- `torch`
- `pynput`

### Install Required Packages
```bash
pip install transformers torch pynput
