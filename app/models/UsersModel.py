from sqlalchemy import Column, Integer, String, Date, Text
from config.connection import Base

class UsersModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225), nullable=False)
    email = Column(Text, nullable=False)
    username = Column(String(225), nullable=False)
    password = Column(Text, nullable=False)
