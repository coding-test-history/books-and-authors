from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.services.AuthorsServices import (
    fetchAllAuthors,
    fetchAuthorById,
    createAuthorService,
    updateAuthorService,
    deleteAuthorService,
    retrieveBooksByAuthor,
)
from app.schemas.AuthorsSchemas import AuthorCreate, AuthorResponse


# get all author
async def getAllAuthors(db: Session):
    return await fetchAllAuthors(db)


# get author by id
async def getAuthorByIdController(id: int, db: Session) -> AuthorResponse:
    """Controller to retrieve author by ID."""
    author = await fetchAuthorById(id, db)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Author not found"
        )
    return author


# Store data
async def createAuthorController(author: AuthorCreate, db: Session) -> AuthorResponse:
    """Controller to handle author creation."""
    return await createAuthorService(author, db)


# Update data
async def updateAuthorController(
    id: int, updatedBook: AuthorCreate, db: Session
) -> AuthorResponse:
    """Controller to handle author update."""
    author = await updateAuthorService(id, updatedBook, db)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Author not found",
        )
    return author


# delete author
def deleteAuthorController(id: int, db: Session):
    """Controller for deleting an author by ID."""
    try:
        result = deleteAuthorService(id, db)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Author not found"
            )
        return None
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}",
        )


# Retrieve all books by a specific author.
async def fetchBooksByAuthor(author_id: int, db: Session):
    """
    Controller to handle fetching books by author ID.
    """
    return await retrieveBooksByAuthor(author_id=author_id, db=db)
