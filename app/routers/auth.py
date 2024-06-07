# app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database
from app.crud.user import get_user_by_email, create_user
from app.dependencies import get_password_hash, create_access_token

# Create a router for authentication-related routes
router = APIRouter()

@router.post("/signup", response_model=schemas.User)
def signup_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """
    Endpoint to create a new user.

    Args:
        user (schemas.UserCreate): The user data for creating a new user.
        db (Session): The database session.

    Returns:
        schemas.User: The created user data.

    Raises:
        HTTPException: If the email is already registered.
    """
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """
    Endpoint to log in a user and get an access token.

    Args:
        user (schemas.UserCreate): The user data for logging in.
        db (Session): The database session.

    Returns:
        dict: A dictionary containing the access token.

    Raises:
        HTTPException: If the credentials are invalid.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if not db_user or not get_password_hash(user.password) == db_user.hashed_password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"token": create_access_token(user.email)}
