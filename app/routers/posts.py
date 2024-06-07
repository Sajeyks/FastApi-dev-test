from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database
from app.dependencies import verify_token
from app.crud.post import now_get_posts, now_create_post
from typing import List  # Import the List type

router = APIRouter()

@router.post("/posts", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, token: str, db: Session = Depends(database.get_db)):
    user = verify_token(token, db)
    print("ID--------------------------------------------",user)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")
    return now_create_post(db=db, post=post, user_id=user.id)

@router.get("/posts", response_model=List[schemas.Post])  # Use the imported List type
def read_posts(token: str, db: Session = Depends(database.get_db)):
    user = verify_token(token, db)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")
    return now_get_posts(db=db)
