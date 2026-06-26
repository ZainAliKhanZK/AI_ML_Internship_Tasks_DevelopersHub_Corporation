import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("HF")

app = FastAPI()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=api_key)

class Request(BaseModel):
    message: str

@app.post("/chat")
def chat(req: Request):
    completion = client.chat.completions.create(
        model="moonshotai/Kimi-K2-Instruct-0905",
        messages=[
            {"role": "system", 
             "content": (
                "You are a helpful and friendly medical assistant."
                "Do not include any medical advice that could be harmful."
                "Keep the responses well structured and clear."
                )
                },
            {
                "role": "user", 
                "content": req.message
            }
        ],
    )

    return {
        "response": completion.choices[0].message.content
    }