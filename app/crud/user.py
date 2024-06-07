# user.py
from sqlalchemy.orm import Session
from app.dependencies import get_password_hash
from app.models import user as models
from app.schemas import user as schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """
    Get a user by email.

    Args:
        db (Session): The database session.
        email (str): The email of the user.

    Returns:
        models.User: The user with the given email or None.
    """
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a new user.

    Args:
        db (Session): The database session.
        user (schemas.UserCreate): The user data.

    Returns:
        models.User: The created user.
    """
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
