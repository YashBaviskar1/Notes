# 📘 FastAPI — Quick Notes

## 1️⃣ What is FastAPI?

A Python framework for building APIs quickly.

- Uses type hints for validation and documentation.
- Built on ASGI (faster than WSGI frameworks like Flask).
- Auto-generates interactive docs:
  - Swagger UI → /docs
  - ReDoc → /redoc

## 2️⃣ Installation

```bash
pip install fastapi uvicorn

```

Run the server:

```bash
uvicorn main:app --reload

# OR

python -m uvicorn main:app --reload

```

## 3️⃣ Creating an App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
return {"message": "Hello World"}

```

## 4️⃣ HTTP Methods

```python
@app.get("/items") # Read
@app.post("/items") # Create
@app.put("/items/{id}") # Update
@app.delete("/items/{id}") # Delete

```

## 5️⃣ Path Parameters

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
return {"item_id": item_id}

```

Type hints (like int) → Auto-validation + docs.

## 6️⃣ Query Parameters

```python
@app.get("/search")
def search(q: str = None, limit: int = 10):
return {"q": q, "limit": limit}

```

Example: /search?q=python&limit=5

## 7️⃣ Request Body (with Pydantic Models)

```python
from pydantic import BaseModel

class Item(BaseModel):
name: str
price: float

@app.post("/items")
def create_item(item: Item):
return {"item": item}

```

FastAPI will auto-validate and show schema in docs.

## 8️⃣ Combining Path, Query & Body

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, q: str, item: Item):
return {"id": item_id, "query": q, "data": item}

```

## 9️⃣ Responses

Return dicts, lists, Pydantic models → FastAPI auto converts to JSON.

Can set custom response codes:

```python
from fastapi import status

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
return item

```

## 🔟 Nested Models

```python
class User(BaseModel):
username: str
email: str

class Post(BaseModel):
title: str
content: str
author: User

```

## 1️⃣1️⃣ Validation with Query/Path Parameters

```python
from fastapi import Query, Path

@app.get("/items/{item_id}")
def read_item(
item_id: int = Path(..., ge=1),
q: str = Query(None, min_length=3)
):
return {"item_id": item_id, "q": q}

```

## 1️⃣2️⃣ Auto Docs

Run server → Go to:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 1️⃣3️⃣ Return JSON

```python
@app.get("/json")
def get_json():
return {"key": "value"}
```

```

No json.dumps() needed — FastAPI does it automatically.

## ✅ In short:

- @app.get/post/put/delete → Routing
- Path params {param} → function(param: type)
- Query params → default values in function args
- Request body → Pydantic model
- Validation → Field, Query, Path
- JSON → Just return dict/list/model
```
