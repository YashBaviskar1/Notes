from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get('/')
def root():
    return {"message" : "Hello World"}

@app.get('/items/{id}')
def read_item(id : int) :
    return {"item_id" : id}


@app.post('/items/')
def create_item(name : str, price : float) :
    return {"name " : name, "price" : price}

@app.get('/users/{user_id}')
def get_users(user_id : int, details : Optional[bool] = False) :
    return {"user_id" : user_id, "deatils" : details}

'''
http://127.0.0.1:8000/users/3?details=True
output : details : true

http://127.0.0.1:8000/users/3?
output : details : false
'''
    
