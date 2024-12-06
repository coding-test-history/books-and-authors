from sqlalchemy import Column, Integer, String, Date, Text
from config.connection import Base

class UsersModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(Text, nullable=False)
