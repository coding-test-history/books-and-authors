from pydantic import BaseModel
from datetime import date


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

    class Config:
        from_attributes = True


class StandardResponse(BaseModel):
    status: int
    message: str
    data: BookResponse | None = None
