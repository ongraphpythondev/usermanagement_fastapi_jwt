from fastapi import FastAPI, Depends, HTTPException, status
from auth import AuthHandler
import schemas
from database import Base, engine, SessionLocal
from models import Users
from typing import List
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)
app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

auth_handler = AuthHandler()

@app.post('/register', status_code=status.HTTP_201_CREATED)
def register(user: schemas.User, session: Session = Depends(get_session)):

    db_user = session.query(Users).filter(Users.username == user.username).first()
    if db_user:
        return HTTPException(status_code=400, detail="Username is taken")
    hashed_password = auth_handler.get_password_hash(user.password)
    db_user = Users(username=user.username,password=hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return {'username':db_user.username,'message':'user created successfully'}



@app.post('/login')
def login(user: schemas.User, session: Session = Depends(get_session)):
    username = user.username
    password = user.password
    db_user = session.query(Users).filter(Users.username == username).first()
    if not db_user:
        raise HTTPException(status_code=401, detail='Invalid username it does not exist')
    if auth_handler.verify_password(password,db_user.password):
        token = auth_handler.encode_token(username)
        return {'message':'logged in successfully', 'token': token }
    return {'message':'provided credentials is not true'}


@app.get('/unprotected')
def unprotected():
    return { 'hello': 'world' }


@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }
