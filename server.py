from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Auralis API running"}

@app.post("/ask")
def ask_ai(query: Query):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": query.question,
            "stream": False
        }
    )

    result = response.json()
    return {"answer": result["response"]}