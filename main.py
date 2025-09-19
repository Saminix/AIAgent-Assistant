
from gpt4all import GPT4All

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")


def prompt():
    prompt = input("Please enter prompt: ")
    return prompt

def generate(prompt):
    with model.chat_session():
        response = model.generate(prompt, max_tokens=150)
        print("Generating answers...")
        print(response)


generate(prompt())

