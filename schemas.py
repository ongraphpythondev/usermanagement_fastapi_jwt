from pydantic import BaseModel


# class UserBase(BaseModel):
#     username: str


class User(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

#another way of defining AuthDetails class
#as we see two attributes of AuthDetails is already present in
#AuthDetailsCreate
"""
class AuthDetails(AuthDetailsCreate):
    id: int

    class Config:
        orm_mode = True
"""
