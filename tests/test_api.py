from fastapi.testclient import TestClient
from api.app import app, assistant
from types import SimpleNamespace

client = TestClient(app)


def test_app_chat_request_return_answer():

    response = SimpleNamespace(content=[SimpleNamespace(
        text="hi hello")], usage=SimpleNamespace(input_tokens=20, output_tokens=10))
    messages = SimpleNamespace(create=lambda **kwargs: response)

    assistant.client = SimpleNamespace(messages=messages)
    assistant.history = []

    resp = client.post("/chat", json={"message": "hello"})

    body = resp.json()

    assert resp.status_code == 200
    assert body["answer"] == "hi hello"
