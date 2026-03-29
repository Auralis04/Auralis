from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    user_message = data.get("message")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are Auralis, a helpful AI assistant for students."},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.json()