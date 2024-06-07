# user.py
from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship
from .post import Post

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    
    posts = relationship("Post", back_populates="owner")
