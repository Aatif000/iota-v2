from fastapi import FastAPI
from pydantic import BaseModel
from llm.chatbot import Chatbot
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")
assistant = Chatbot(key)


class ChatRequest(BaseModel):  # it says what the client must send
    message: str


@app.post("/chat")  # this is the url path and http method
def chat(req: ChatRequest):
    user_message = req.message
    response = assistant.send_message(user_message)
    return response
