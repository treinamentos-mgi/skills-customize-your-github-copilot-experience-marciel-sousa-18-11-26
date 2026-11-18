from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookInput(BaseModel):
    title: str
    author: str


books = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="A Wizard of Earthsea", author="Ursula K. Le Guin"),
]
next_book_id = 3

# Add the API routes described in the assignment below.