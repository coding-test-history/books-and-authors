from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.services.BooksServices import (
    fetchAllBooks,
    fetchBookById,
    createBookService,
    updateBookService,
    deleteBookService,
)
from app.schemas.BooksSchemas import BookCreate, BookResponse


# Retrieve a list of all books
async def getAllBooks(db: Session):
    return await fetchAllBooks(db)


# Retrieve details of a specific book.
async def getBookByIdController(id: int, db: Session) -> BookResponse:
    """Controller to retrieve book by ID."""
    book = await fetchBookById(id, db)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


# Create a new book.
async def createBookController(book: BookCreate, db: Session) -> BookResponse:
    """Controller to handle book creation."""
    return await createBookService(book, db)


# Update an existing book.
async def updateBookController(
    id: int, updatedBook: BookCreate, db: Session
) -> BookResponse:
    """Controller to handle book update."""
    book = await updateBookService(id, updatedBook, db)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    return book


# delete a book
def deleteBookController(id: int, db: Session):
    """Controller for deleting an book by ID."""
    try:
        result = deleteBookService(id, db)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )
        return None
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}",
        )