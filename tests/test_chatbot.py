from llm.chatbot import Chatbot
from types import SimpleNamespace


def test_send_message_stores_history():
    bot = Chatbot("fake-key")

    response = SimpleNamespace(content=[SimpleNamespace(
        text="hi hello")], usage=SimpleNamespace(input_tokens=20, output_tokens=10))
    fake_create = lambda **kwargs: response
    messages = SimpleNamespace(create=fake_create)
    client = SimpleNamespace(messages=messages)

    bot.client = client

    call_bot = bot.send_message("hi")

    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"
    assert call_bot["answer"] == "hi hello"
