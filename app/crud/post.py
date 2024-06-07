from sqlalchemy.orm import Session
from app.models import post as models
from app.schemas import post as schemas

def now_get_posts(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of posts from the database.

    Args:
        db (Session): The database session.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to return.

    Returns:
        List[models.Post]: A list of post objects.
    """
    return db.query(models.Post).offset(skip).limit(limit).all()

def now_create_post(db: Session, post: schemas.PostCreate, user_id: int):
    """
    Create a new post and save it to the database.

    Args:
        db (Session): The database session.
        post (schemas.PostCreate): The data for creating a new post.
        user_id (int): The ID of the user creating the post.

    Returns:
        models.Post: The created post object.
    """
    db_post = models.Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
