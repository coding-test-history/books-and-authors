from pydantic import BaseModel
from datetime import date

class AuthorBase(BaseModel):
    name: str
    bio: str | None = None
    birth_date: date | None = None

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int

    class Config:
        from_attributes = True

class StandardResponse(BaseModel):
    status: int
    message: str
    data: AuthorResponse | None = None