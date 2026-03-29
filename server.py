from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()

    user_message = data.get("message")
    chat_history = data.get("history", [])

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {
            "role": "system",
            "content": "You are Auralis, an AI assistant for GITAM University. Answer clearly and help students."
        }
    ] + chat_history + [
        {"role": "user", "content": user_message}
    ]

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": messages
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.json()