from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Text


class Post(Base):
    """
    Represents a post in the database.

    Attributes:
        id (int): The unique identifier for the post.
        text (str): The content of the post.
        owner_id (int): The ID of the user who created the post.
        owner (relationship): Relationship with the User model indicating the owner of the post.
    """
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")
