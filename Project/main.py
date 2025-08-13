from fastapi import FastAPI
from pydantic import BaseModel, Field
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv
from groq import Groq
from typing import Optional

class Settings(BaseSettings) :
    API_KEY : str
    class Config :
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

client = Groq(api_key=settings.API_KEY)
app = FastAPI()

class Text(BaseModel) :
    text : str = Field(..., min_length=50)
    amt_of_chracters : Optional[int] = Field(default=None,gt = 0)


def LLM_integration(text_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"summarize this text {text_input}",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content



@app.post('/summarize/')
def summarize(payload : Text) :
    ##### ITERATION 1 of summarization to return first N chracters 
    summary = payload.text[:payload.amt_of_chracters]

    return {"text" : payload.text,  "summary" : summary, "original_length" : len(payload.text), "summary_length" : len(summary)}


@app.post('/summarize_llm/')
def summarize_llm(payload : Text) :
    ##### ITERATION 1 of summarization to return first N chracters 
    summary = LLM_integration(payload.text)
    return {"text" : payload.text,  "summary" : summary, "original_length" : len(payload.text), "summary_length" : len(summary)}
