# 📒 Pydantic Basics Notes

## 1. What is Pydantic?

Python library for data validation and type enforcement.

Works by creating models (classes) with defined fields and rules.

Automatically:

- Checks if incoming data matches expected types.
- Converts types when possible.
- Raises clear errors if invalid.

## 2. Why use Pydantic?

- Avoids writing manual if checks for every field.
- Ensures consistent data structure in your app.
- Integrates perfectly with FastAPI for request validation & auto-generated docs.

## 3. How to think when creating models

- What fields are needed?
- What type is each field (str, int, list, etc.)?
- Required or optional?
- Any constraints?
  - String length
  - Number range
  - List size
  - Regex pattern
- Any default values?
- Any nested models needed?

## 4. Field() — The Control Panel

Field() is used to:

### Set required/optional

- `Field(...)` → Required
- `Field(default)` → Optional with default value
- `Field(None)` → Optional, default None

### Add constraints

- `min_length`, `max_length` → strings/lists
- `ge (≥)`, `le (≤)` → numbers
- `min_items`, `max_items` → lists
- `regex` → match patterns

### Add metadata (used in API docs)

- `title`, `description`, `example`

### Combine defaults + constraints

`Field(0, ge=0, le=100)`

## 5. Example Implementation

```python
from pydantic import BaseModel, Field
from typing import List, Optional

class Book(BaseModel):
    title: str = Field(..., min_length=2, max_length=100) # required, 2-100 chars
    author: str = Field(..., min_length=2, max_length=50) # required, 2-50 chars
    price: float = Field(..., ge=0) # required, >= 0
    in_stock: bool = Field(True) # optional, defaults to True
    tags: Optional[List[str]] = Field(None, max_items=5) # optional list, max 5 items
    isbn: str = Field(..., min_length=13, max_length=13) # required, exactly 13 chars

book1 = Book(
    title="1984",
    author="George Orwell",
    price="499.99", # auto-converted to float
    tags=["Dystopia", "Fictional"],
    isbn="1234567890123"
)

print(book1.dict())
```

# 📒 Pydantic Notes — Validators, Nested Models, and JSON

## 1. Validators in Pydantic

Validators allow you to add custom validation logic beyond the built-in constraints from Field().

### Types

- Pydantic v1 used @validator — deprecated in v2.
- Pydantic v2 uses @field_validator.

### Field Constraints vs Validators

| Feature    | Field() constraints            | @field_validator                      |
| ---------- | ------------------------------ | ------------------------------------- |
| Purpose    | Simple, declarative validation | Complex, custom validation            |
| Examples   | min_length, ge, le, regex, gt  | Cross-field checks, conditional rules |
| Execution  | Runs before assigning value    | Runs after basic type validation      |
| Complexity | Simple checks only             | Access to class, value, other fields  |

### Parameters in @field_validator

```python
@field_validator("field_name")
def my_validator(cls, v):
    ...
```

- cls → The model class. Lets you access class-level attributes if needed.
- v → The value of the field being validated (already type-checked).
- values (optional, only if mode="before" or mode="after" with config) → Dict of previously validated fields in the same model.

⚠ Order matters — only fields defined above in the class are available here.

### Example:

```python
class Registration(BaseModel):
    attendee: Attendee
    sessions: List[Session]

    @field_validator("sessions")
    def check_sessions(cls, v, values):
        # Access another field if needed
        attendee = values.get("attendee")
        if len(v) < 1:
            raise ValueError(f"{attendee.name} must register for at least one session")
        return v
```

## 2. Nested Models

Pydantic allows models inside other models for structured validation.

### Example:

```python
class Attendee(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., ge=18)

class Session(BaseModel):
    title: str
    speaker: str
    duration_minutes: int = Field(..., gt=0)

class Registration(BaseModel):
    attendee: Attendee
    sessions: List[Session]
```

- Pydantic automatically validates nested models.
- You can pass dicts instead of model instances, Pydantic will parse them.

## 3. Converting to JSON

Pydantic v2 uses:

```python
model.model_dump_json(indent=2)
```

- model_dump_json() → returns JSON string.
- model_dump() → returns Python dict.

### Example:

```python
reg = Registration(
    attendee=Attendee(name="YGB", email="yash@gmail.com", age=22),
    sessions=[
        Session(title="RAG", speaker="YGGB", duration_minutes=120),
        Session(title="RAG2", speaker="YGGB", duration_minutes=120)
    ]
)

print(reg.model_dump_json(indent=2))
```

### Output:

```json
{
  "attendee": {
    "name": "YGB",
    "email": "yash@gmail.com",
    "age": 22
  },
  "sessions": [
    {
      "title": "RAG",
      "speaker": "YGGB",
      "duration_minutes": 120
    },
    {
      "title": "RAG2",
      "speaker": "YGGB",
      "duration_minutes": 120
    }
  ]
}
```

## ✅ Key Takeaways

- Use Field() for simple constraints, @field_validator for complex logic.
- Validators in v2 are @field_validator (v1 style is deprecated).
- values lets you reference previously validated fields (order matters).
- Nested models make structured, reusable validation easy.
- Use .model_dump_json() for JSON output and .model_dump() for dicts.
