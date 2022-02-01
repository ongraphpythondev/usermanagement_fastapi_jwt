from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///user.db")
#other way of doing the above task
"""
SQLALCHEMY_DATABASE_URL = "sqlite:///user.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})
"""

SessionLocal = sessionmaker(bind=engine,expire_on_commit=False)

Base = declarative_base()
