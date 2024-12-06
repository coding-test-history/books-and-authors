from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.BooksModel import BooksModel
from fastapi import HTTPException, status
from app.schemas.BooksSchemas import BookResponse, BookCreate


# Retrieve a list of all books
async def fetchAllBooks(db: Session):
    try:
        booksData = db.query(BooksModel).all()
        return {"status": status.HTTP_200_OK, "message": "OK", "data": booksData}
    except SQLAlchemyError as e:
        # Log error here if logging is implemented
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch books from the database.",
        )


# Retrieve details of a specific book.
async def fetchBookById(book_id: int, db: Session):
    """Service to fetch book by ID from the database."""
    try:
        booksData = db.query(BooksModel).filter(BooksModel.id == book_id).first()
        if not booksData:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )
        # Convert SQLAlchemy object to Pydantic model

        return {
            "status": status.HTTP_200_OK,
            "message": "OK",
            "data": BookResponse.from_orm(booksData),
        }
    except SQLAlchemyError as e:
        # Log error if a logging mechanism is implemented
        raise Exception("Failed to fetch book from the database.")


# Create a new book.
async def createBookService(book: BookCreate, db: Session):
    """Service to create a new book in the database."""
    try:
        db_book = BooksModel(
            title=book.title,
            description=book.description,
            publish_date=book.publish_date,
            author_id=book.author_id,
        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return {"status": status.HTTP_201_CREATED, "message": "Created"}
    except SQLAlchemyError as e:
        raise Exception("Failed to create a new book.")


# Update an existing book.
async def updateBookService(id: int, updatedBook: BookCreate, db: Session):
    """Service to update an existing book in the database."""
    try:
        book = db.query(BooksModel).filter(BooksModel.id == id).first()
        if not book:
            return None
        book.title = updatedBook.title
        book.description = updatedBook.description
        book.publish_date = updatedBook.publish_date
        book.author_id = updatedBook.author_id
        db.commit()
        db.refresh(book)
        return {"status": status.HTTP_200_OK, "message": "OK"}
    except SQLAlchemyError as e:
        raise Exception("Failed to update the book.")


# delete a book
def deleteBookService(id: int, db: Session) -> bool:
    """Service for deleting an book by ID."""
    try:
        book = db.query(BooksModel).filter(BooksModel.id == id).first()
        if not book:
            return False
        db.delete(book)
        db.commit()
        return True
    except Exception as e:
        # Log error if needed
        print(f"Error deleting book: {str(e)}")
        raise e