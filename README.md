# Discord Typing Bot (GPT-2 Powered)
## **I WILL NOT HELP YOU WITH ANYTHING**

This script generates text using GPT-2 and types it out in Discord or any text field by simulating keyboard inputs. The goal? Send ridiculous AI-generated messages automatically.

---

## What This Does
- Uses GPT-2 to generate random text.  
- Simulates typing with `pynput`.  
- Automatically sends messages by pressing Enter.  
- Builds on the previous message to create longer, chaotic stories.  

---

## Dependencies
You'll need these installed:  
- **Python 3.8+**  
- **transformers** – Loads GPT-2 from Hugging Face.  
- **torch** – Required for GPT-2 to function.  
- **pynput** – Simulates keyboard input.  

Install with:  
```bash
pip install transformers torch pynput
