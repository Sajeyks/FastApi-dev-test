# app/schemas/user.py

from pydantic import BaseModel

class UserBase(BaseModel):
    """
    Base schema for User, includes common attributes.
    """
    email: str

class UserCreate(UserBase):
    """
    Schema for creating a new User, includes password.
    """
    password: str

class User(UserBase):
    """
    Schema for returning User data, includes id.
    """
    id: int

    class Config:
        """
        Configuration for Pydantic model to support ORM mode.
        """
        orm_mode = True
