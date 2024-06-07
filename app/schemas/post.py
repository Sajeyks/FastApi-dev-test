from pydantic import BaseModel

class PostBase(BaseModel):
    """
    Base model for a post.

    Attributes:
        text (str): The text content of the post.
    """
    text: str

class PostCreate(PostBase):
    """
    Model for creating a post, inherits from PostBase.
    """
    pass

class Post(PostBase):
    """
    Model representing a post.

    Attributes:
        id (int): The unique identifier for the post.
        owner_id (int): The ID of the user who created the post.
    """
    id: int
    owner_id: int

    class Config:
        orm_mode = True
