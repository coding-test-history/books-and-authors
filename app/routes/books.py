from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.dependencies import get_db
from app.schemas.BooksSchemas import BookCreate, BookResponse, StandardResponse
from app.controllers.BooksController import (
    getAllBooks,
    getBookByIdController,
    createBookController,
    updateBookController,
    deleteBookController
)


router = APIRouter()


# Retrieve a list of all books
@router.get("/", summary="Retrieve all books")
async def getBooksRoute(db=Depends(get_db)):
    return await getAllBooks(db)


# Retrieve details of a specific book.
@router.get("/{id}", response_model=StandardResponse, summary="Retrieve book by ID")
async def getBookByIdRoute(id: int, db: Session = Depends(get_db)):
    """Route to retrieve book by ID."""
    return await getBookByIdController(id, db)


# Create a new book.
@router.post(
    "/store",
    response_model=StandardResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new book",
)
async def createBookRoute(book: BookCreate, db: Session = Depends(get_db)):
    """Route to create a new book."""
    return await createBookController(book, db)


# Update an existing book.
@router.put(
    "/update/{id}", response_model=StandardResponse, summary="Update an existing book"
)
async def updateBookRoute(
    id: int, updatedBook: BookCreate, db: Session = Depends(get_db)
):
    """Route to update an existing book's details."""
    return await updateBookController(id, updatedBook, db)


# delete a book
@router.delete(
    "/delete/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete an book"
)
def deleteBook(id: int, db: Session = Depends(get_db)):
    """Delete an book by ID."""
    return deleteBookController(id, db)