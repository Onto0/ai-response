# Discord Typing Bot (GPT-2 Powered)

This script generates random, often ridiculous responses using GPT-2 and simulates typing them out in Discord or any text input field. If you're here, you probably know what you're doing—or you’re about to learn the hard way.

## What This Does
- Generates text with GPT-2 (Hugging Face).
- Types it out character by character, simulating real typing.
- Automatically presses Enter to send messages.
- Repeats for a fixed number of messages to build a chaotic story.

---

## Dependencies (Figure It Out Yourself)
You're going to need a few things installed. I won't walk you through it.

- **Python 3.8+** – If you don’t have Python, go get it.
- **transformers** – By Hugging Face. It’s how you load GPT-2.
- **torch** – PyTorch. GPT-2 won’t work without it.
- **pynput** – This lets the script simulate key presses.

### Install the Requirements
If you actually need help:
```bash
pip install transformers torch pynput
