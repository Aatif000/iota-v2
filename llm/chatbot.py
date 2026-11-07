import anthropic
import time


class Chatbot:
    def __init__(self, API_KEY, model="claude-haiku-4-5-20251001", system_prompt="You are a helpful assistant"):
        self.api_key = API_KEY
        self.history = []
        self.client = anthropic.Anthropic(api_key=API_KEY)
        self.model = model
        self.system_prompt = system_prompt

    def send_message(self, user_input):

        system_activity = {
            "answer": None,
            "input_token_count": None,
            "output_token_count": None,
            "latency": None
        }

        start_time = time.perf_counter()

        self.history.append({"role": "user", "content": user_input})
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=self.history[-15:],
            system=self.system_prompt
        )
        system_activity["answer"] = response.content[0].text
        self.history.append(
            {"role": "assistant", "content": response.content[0].text})

        end_time = time.perf_counter()

        system_activity["input_token_count"] = response.usage.input_tokens
        system_activity["output_token_count"] = response.usage.output_tokens

        system_activity["latency"] = end_time - start_time

        return system_activity
