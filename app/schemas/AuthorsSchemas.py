from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Generic, TypeVar

# Base schema for Author
class AuthorBase(BaseModel):
    name: str
    bio: str
    birth_date: date

# Schema for creating an Author
class AuthorCreate(AuthorBase):
    pass

# Schema for returning an Author
class AuthorResponse(AuthorBase):
    id: int

    # Configuration for compatibility with ORM models
    model_config = ConfigDict(from_attributes=True)

# Generic StandardResponse schema
T = TypeVar("T")  # Generic type variable

class StandardResponse(BaseModel, Generic[T]):  # Note: BaseModel comes first
    status: int
    message: str
    data: T | None = None
