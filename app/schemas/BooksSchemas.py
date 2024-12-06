from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Generic, TypeVar


class BookBase(BaseModel):
    title: str
    description: str
    publish_date: date
    author_id: int


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
    author_id: int

    # Configuration for compatibility with ORM models
    model_config = ConfigDict(from_attributes=True)


# Generic StandardResponse schema
T = TypeVar("T")  # Generic type variable


class StandardResponse(BaseModel, Generic[T]):  # Note: BaseModel comes first
    status: int
    message: str
    data: T | None = None
