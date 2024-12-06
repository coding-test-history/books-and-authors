from pydantic import BaseModel
from datetime import date

class BookBase(BaseModel):
    title: str
    description: str
    publish_date: date

class BookResponse(BookBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True
