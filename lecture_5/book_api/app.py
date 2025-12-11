from fastapi import FastAPI
from typing import Optional

import uvicorn

from database.creating_db import Book, session
from database.schemes import BookCreate, BookUpdate

app = FastAPI()

@app.post("/books/")
def add_new_book(book : BookCreate):
    new_book = Book(title = book.title, author = book.author, year = book.year)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book

@app.get("/books/")
def get_all_books():
    books = session.query(Book).all()
    return books

@app.delete("/books/{book_id}/")
def delete_book(book_id : int):
    book = session.query(Book).filter_by(id = book_id).first()
    session.delete(book)
    session.commit()

@app.put("/books/{book_id}/")
def update_book_details(book_id : int, update_book : BookUpdate):
    book = session.query(Book).filter_by(id = book_id).first()
    book.title = update_book.title
    book.author = update_book.author
    book.year = update_book.year
    session.commit()
    session.refresh(book)

@app.get("/books/search/")
def update_book_details(title: Optional[str] = None, author: Optional[str] = None, year:  Optional[int] = None):
    book = session.query(Book)
    if title:
        book = book.filter_by(title = title)
    if author:
        book = book.filter_by(author = author)
    if year:
        book = book.filter_by(year = year)
    return book.first()

if __name__ == '__main__':
    uvicorn.run("app:app", reload=True)