from fastapi import FastAPI, HTTPException
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


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books():
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_input: BookInput):
    next_id = max((book.id for book in books), default=0) + 1
    book = Book(id=next_id, **book_input.model_dump())
    books.append(book)
    return book