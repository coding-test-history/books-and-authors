from sqlalchemy import Column, Integer, String, Date, Text, TIMESTAMP
from config.connection import Base


class BooksModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225), nullable=False)
    description = Column(Text, nullable=False)
    publish_date = Column(TIMESTAMP, nullable=False)
    author_id = Column(Integer, nullable=False)
