from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv
from typing import Optional, List
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor




class Settings(BaseSettings) :
    API_KEY : str
    class Config :
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

#client = Groq(api_key=settings.API_KEY)
app = FastAPI()



class Text(BaseModel) :
    text : str = Field(..., min_length=50)
    amt_of_chracters : Optional[int] = Field(default=None,gt = 0)
    question : Optional[str] = Field(default=None)  


class Document(BaseModel) :
    texts : List[str] = Field(..., min_items = 1)

def templates(agent_call : str) :
    template_for_summarization = """
    You are a summarizer agent who has to summarize the text and restrict it to specific N words.
    if there is "any number of words" you can 
    Text to summarize : {text}
    Size Constraint : {number} of words
    """
    template_for_ask = """
    You are supposed to answer the user's query for given question based on the context avaliable 
    from you to answer from, stick to the context while answering user's query
    text to ask from : {text} 
    question : {question}
    """
    if agent_call == "summary" :
        return template_for_summarization
    elif agent_call == "ask" : 
        return template_for_ask
    

def write_in_logs(log) :
    with open("logs.txt", "a")  as file :
        file.write(f"\n{log}")

@app.middleware('http')
async def log_processing_time(request : Request, call_next) :
    start_time = time.time()
    response = await call_next(request)
    final_time = time.time()
    print(final_time - start_time)
    log = f"{datetime.now()}\tRequest : {request.method} {request.url.path} | start time : {start_time} | final time : {final_time} | Processing time : {final_time - start_time}"
    write_in_logs(log)
    return response


def LLM_integration(text_input : str, template_type : str, number_of_words : int | str = None, question : str = None ):
    llm = ChatGroq(api_key = settings.API_KEY, model="llama-3.3-70b-versatile", temperature=0.8)
    if template_type == "summary" :
        prompt = PromptTemplate.from_template(templates(template_type)).format(text=text_input, number=number_of_words)
    elif template_type == "ask" : 
        prompt = PromptTemplate.from_template(templates(template_type)).format(text=text_input, question=question)        
    response = llm.invoke(prompt)
    return response.content


@app.post('/summarize/')
def summarize(payload : Text) :
    ##### ITERATION 1 of summarization to return first N chracters 
    summary = payload.text[:payload.amt_of_chracters]

    return {"text" : payload.text,  "summary" : summary, "original_length" : len(payload.text), "summary_length" : len(summary)}


@app.post('/summarize_llm/')
def summarize_llm(payload : Text) :
    amt = payload.amt_of_chracters if payload.amt_of_chracters is not None else "any"
    summary = LLM_integration(payload.text, template_type="summary", number_of_words=amt)
    return {"text" : payload.text,  "summary" : summary, "original_length" : len(payload.text), "summary_length" : len(summary)}


@app.post('/ask')
def ask_llm(payload : Text) :
    question = payload.question if payload.question is not None else "please ask question"
    response = LLM_integration(payload.text, "ask", question=question)
    return {"text": payload.text, "question": question, "response" : response}

##### ITERATION 1 ######
@app.post('/bulk_summarizer/')
def bulk_summarizer(payload : Document) :
    results = []
    for text in payload.texts : 
        results.append({
            "text" : text,
            "summary" : LLM_integration(text, "summary")
        })
    
    return results


##### ITERATION 2 ########
@app.post('/bulk_summarizer2/')
def bulk_summarizer2(payload : Document) :
    result_iterator = []
    with ThreadPoolExecutor(max_workers=6) as execuator : 
        result_iterator = execuator.map(LLM_integration, payload.texts, ["summary"]*len(payload.texts))
    results = list(result_iterator)
    return { "results" : results}
