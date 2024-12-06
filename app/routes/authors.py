from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.dependencies import get_db
from app.models.AuthorsModel import AuthorsModel
from app.schemas.AuthorsSchemas import AuthorCreate, AuthorResponse, StandardResponse
from app.controllers.AuthorsController import (
    getAllAuthors,
    getAuthorByIdController,
    createAuthorController,
    updateAuthorController,
    deleteAuthorController,
)


router = APIRouter()


# get all author
@router.get("/", summary="Retrieve all authors")
async def getAuthorsRoute(db=Depends(get_db)):
    return await getAllAuthors(db)


# get author by id
@router.get("/{id}", response_model=StandardResponse, summary="Retrieve author by ID")
async def getAuthorByIdRoute(id: int, db: Session = Depends(get_db)):
    """Route to retrieve author by ID."""
    return await getAuthorByIdController(id, db)


# Store data
@router.post(
    "/store",
    response_model=StandardResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new author",
)
async def createAuthorRoute(author: AuthorCreate, db: Session = Depends(get_db)):
    """Route to create a new author."""
    return await createAuthorController(author, db)


# Update data
@router.put(
    "/update/{id}", response_model=StandardResponse, summary="Update an existing author"
)
async def updateAuthorRoute(
    id: int, updated_author: AuthorCreate, db: Session = Depends(get_db)
):
    """Route to update an existing author's details."""
    return await updateAuthorController(id, updated_author, db)


# delete author
@router.delete(
    "/delete/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete an author"
)
def deleteAuthor(id: int, db: Session = Depends(get_db)):
    """Delete an author by ID."""
    return deleteAuthorController(id, db)
