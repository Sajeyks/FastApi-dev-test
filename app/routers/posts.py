from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database
from app.dependencies import verify_token
from app.crud.post import now_get_posts, now_create_post
from typing import List

router = APIRouter()

@router.post("/posts", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, token: str, db: Session = Depends(database.get_db)):
    """
    Endpoint to create a new post.

    Args:
        post (schemas.PostCreate): The data for creating a new post.
        token (str): The access token for authentication.
        db (Session): The database session.

    Returns:
        schemas.Post: The created post.

    Raises:
        HTTPException: If the token is invalid.
    """
    user = verify_token(token, db)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")
    return now_create_post(db=db, post=post, user_id=user.id)

@router.get("/posts", response_model=List[schemas.Post])
def read_posts(token: str, db: Session = Depends(database.get_db)):
    """
    Endpoint to retrieve posts.

    Args:
        token (str): The access token for authentication.
        db (Session): The database session.

    Returns:
        List[schemas.Post]: A list of posts.

    Raises:
        HTTPException: If the token is invalid.
    """
    user = verify_token(token, db)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")
    return now_get_posts(db=db)
