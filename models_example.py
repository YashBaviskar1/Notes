from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import List, Optional
### Defining Base Models for Book, A Aimple implementation of Pydantic model 
class Book(BaseModel) :
    title : str = Field(..., min_length=2, max_length=100)
    author : str = Field(..., min_length=2, max_length=50)
    price : float = Field(..., ge=0)
    in_stock : bool = Field(True)
    tags : Optional[List[str]] = Field(None, max_items = 5)
    isbn : str = Field(..., min_length=13, max_length=13)


book1 = Book(title="1984", author="Geroge Orwell", price="499.99", tags=["Dystopia", "Fictional"], isbn="1234567890123")

# print(book1.dict())


#### model for Conferance Resgistration API 

class Attendee(BaseModel) :
    name : str  = Field(..., min_length = 2)
    email : EmailStr
    age : int = Field(..., ge = 18)

class Session(BaseModel) :
    title : str = Field(...)
    speaker : str = Field(...)
    duration_mins : int = Field(gt = 0)

class Registration(BaseModel) :
    attendee : Attendee
    sessions : List[Session]
    @field_validator("sessions")
    def chec_attendee(cls, v) :
        if len(v) < 1 :
            raise ValueError("sessions should be more than 1")
        return v 

reg = Registration(
    attendee = Attendee(name="YGB", email="yash@gmail.com", age = 22),
    sessions = [Session(title="RAG", speaker="YGGB", duration_mins=120), Session(title="RAG2", speaker="YGGB", duration_mins=120)]
)
print(reg.model_dump_json(indent=2))



