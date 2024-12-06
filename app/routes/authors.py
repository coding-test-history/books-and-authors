from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.dependencies import get_db
from app.models.AuthorsModel import AuthorsModel
from app.schemas.AuthorsSchemas import AuthorCreate, AuthorResponse

router = APIRouter()

# @router.get("/", response_model=list[AuthorResponse], summary="Retrieve all authors")
# def get_authors(db: Session = Depends(get_db)):
#     """Retrieve a list of all authors."""
#     authors = db.query(AuthorsModel).all()
#     return authors

# @router.get("/{id}", response_model=AuthorResponse, summary="Retrieve author by ID")
# def get_author_by_id(id: int, db: Session = Depends(get_db)):
#     """Retrieve details of a specific author by ID."""
#     author = db.query(AuthorsModel).filter(AuthorsModel.id == id).first()
#     if not author:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
#     return author

# @router.post("/", response_model=AuthorResponse, status_code=status.HTTP_201_CREATED, summary="Create a new author")
# def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
#     """Create a new author."""
#     db_author = AuthorsModel(name=AuthorsModel.name, bio=AuthorsModel.bio, birth_date=AuthorsModel.birth_date)
#     db.add(db_author)
#     db.commit()
#     db.refresh(db_author)
#     return db_author

# @router.put("/{id}", response_model=AuthorResponse, summary="Update an existing author")
# def update_author(id: int, updated_author: AuthorCreate, db: Session = Depends(get_db)):
#     """Update an existing author's details."""
#     author = db.query(AuthorsModel).filter(AuthorsModel.id == id).first()
#     if not author:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
#     AuthorsModel.name = updated_author.name
#     AuthorsModel.bio = updated_author.bio
#     AuthorsModel.birth_date = updated_author.birth_date
#     db.commit()
#     db.refresh(author)
#     return author

# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete an author")
# def delete_author(id: int, db: Session = Depends(get_db)):
#     """Delete an author by ID."""
#     author = db.query(AuthorsModel).filter(AuthorsModel.id == id).first()
#     if not author:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
#     db.delete(author)
#     db.commit()
#     return None
