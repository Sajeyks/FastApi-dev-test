from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship
from .post import Post

class User(Base):
    """
    Represents a user in the database.

    Attributes:
        id (int): The unique identifier for the user.
        email (str): The email address of the user (unique).
        hashed_password (str): The hashed password of the user.
        posts (relationship): Relationship with the Post model indicating posts created by the user.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    
    posts = relationship("Post", back_populates="owner")
