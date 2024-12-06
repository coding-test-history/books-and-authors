from sqlalchemy import Column, Integer, String, Date
from config.connection import Base

class AuthorsModel(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    bio = Column(String, nullable=True)
    birth_date = Column(Date, nullable=True)
