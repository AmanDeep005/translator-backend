from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq

import os
from dotenv import load_dotenv


load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
app =FastAPI()

@app.get("/amit")
async def amit_function():
    return {"message": "Amit to rand hai"}

class theinput(BaseModel):
    text: str

@app.post("/translator")
async def duhan(request: theinput):
    completion = client.chat.completions.create(
        model="llama-3.2-90b-vision-preview",
        messages=[
             {"role": "system", "content": "You are a professional translator. Your task is to translate English text to Hindi. Provide only the Hindi translation without any additional explanations or notes."},
                {"role": "user", "content": f"Translate the following English text to Hindi: {request.text}"}
        ],
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        stream=False  # to get full response at once
    )

    answer = completion.choices[0].message.content if completion.choices else None

    return {"answer": answer}