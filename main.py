import os
from llm.chatbot import Chatbot
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")

assistant = Chatbot(key)

user_input = input("Ask away...\n")

while True:
    try:
        if user_input.lower() == "quit":
            break
        response = assistant.send_message(user_input)
        print(response["answer"])
        print(f"Input token count: {response['input_token_count']}")
        print(f"Output token count: {response['output_token_count']}")
        print(f"Latency: {response['latency']:.2f}")

        user_input = input("")
    except Exception as e:
        print("Code failed:", e)
        user_input = input("Something went wrong! Try again.\n")
