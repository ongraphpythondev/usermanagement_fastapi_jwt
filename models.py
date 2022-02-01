from sqlalchemy import Column, Integer, String
from database import Base

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))
