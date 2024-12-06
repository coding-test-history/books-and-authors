from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.AuthorsModel import AuthorsModel
from app.models.BooksModel import BooksModel
from fastapi import HTTPException, status
from app.schemas.AuthorsSchemas import AuthorCreate, AuthorResponse
from app.schemas.BooksSchemas import BookResponse


# get all author
async def fetchAllAuthors(db: Session):
    try:
        authorData = db.query(AuthorsModel).all()
        return {"status": status.HTTP_200_OK, "message": "OK", "data": authorData}
    except SQLAlchemyError as e:
        # Log error here if logging is implemented
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch authors from the database.",
        )


# get author by id
async def fetchAuthorById(author_id: int, db: Session):
    """Service to fetch author by ID from the database."""
    try:
        authorData = db.query(AuthorsModel).filter(AuthorsModel.id == author_id).first()
        if not authorData:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Author not found"
            )
        # Convert SQLAlchemy object to Pydantic model

        return {
            "status": status.HTTP_200_OK,
            "message": "OK",
            "data": AuthorResponse.from_orm(authorData),
        }
    except SQLAlchemyError as e:
        # Log error if a logging mechanism is implemented
        raise Exception("Failed to fetch author from the database.")


# Store data
async def createAuthorService(author: AuthorCreate, db: Session):
    """Service to create a new author in the database."""
    try:
        db_author = AuthorsModel(
            name=author.name,
            bio=author.bio,
            birth_date=author.birth_date,
        )
        db.add(db_author)
        db.commit()
        db.refresh(db_author)
        return {"status": status.HTTP_201_CREATED, "message": "Created"}
    except SQLAlchemyError as e:
        raise Exception("Failed to create a new author.")


# Update data
async def updateAuthorService(id: int, updatedAuthor: AuthorCreate, db: Session):
    """Service to update an existing author in the database."""
    try:
        author = db.query(AuthorsModel).filter(AuthorsModel.id == id).first()
        if not author:
            return None
        author.name = updatedAuthor.name
        author.bio = updatedAuthor.bio
        author.birth_date = updatedAuthor.birth_date
        db.commit()
        db.refresh(author)
        return {"status": status.HTTP_200_OK, "message": "OK"}
    except SQLAlchemyError as e:
        raise Exception("Failed to update the author.")


# delete author
def deleteAuthorService(id: int, db: Session) -> bool:
    """Service for deleting an author by ID."""
    try:
        author = db.query(AuthorsModel).filter(AuthorsModel.id == id).first()
        if not author:
            return False
        db.delete(author)
        db.commit()
        return True
    except Exception as e:
        # Log error if needed
        print(f"Error deleting author: {str(e)}")
        raise e


# Retrieve all books by a specific author.
async def retrieveBooksByAuthor(author_id: int, db: Session):
    """
    Service to retrieve all books by a specific author from the database.
    """
    try:
        books = db.query(BooksModel).filter(BooksModel.author_id == author_id).all()
        booksResponse = [BookResponse.from_orm(book) for book in books]
        if not books:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No books found for the specified author.",
            )
        return {
            "status": status.HTTP_200_OK,
            "message": "Books retrieved successfully.",
            "data": booksResponse,
        }
    except SQLAlchemyError:
        # Log error if necessary
        raise Exception("Failed to fetch books by author from the database.")
