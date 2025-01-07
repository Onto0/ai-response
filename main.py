import random
import time
from pynput.keyboard import Controller, Key
from transformers import GPT2LMHeadModel, GPT2Tokenizer

keyboard = Controller()
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

tokenizer.pad_token = tokenizer.eos_token  # Set pad token explicitly


def ridiculous_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    outputs = model.generate(
        inputs,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
        max_new_tokens=100  # Prioritize this over max_length
    )

    message = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return message.strip()


def type_message(message):
    print(f"Typing message: {message}")
    for char in message:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.04)  # Increased delay for stability


def send_message():
    try:
        start_message = input("Enter the starting sentence of the story: ")

        # Generate continuation immediately using the starting sentence
        full_story = ridiculous_response(start_message)

        # Send the generated continuation right away
        type_message(full_story)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        # Continue evolving the story
        for _ in range(3):  # Send 3 more messages
            time.sleep(5)
            full_story += " " + ridiculous_response(full_story)
            type_message(full_story)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting gracefully...")


send_message()
