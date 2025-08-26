from ollama import chat
from langchain_ollama import ChatOllama

response = chat(model = "gemma3:1b", messages= [{
    'role' : 'user', 
    'message' : 'Who are you?',
    }] )


llm = ChatOllama(
    model = 'gemma3:1b',
)

response = llm.invoke("who are you")
print(response.content)