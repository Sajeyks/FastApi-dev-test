from fastapi import FastAPI
from app.routers import auth, posts

app = FastAPI()

# Include the auth and posts routers
app.include_router(auth.router)
app.include_router(posts.router)

@app.on_event("startup")
async def startup_event():
    """
    Event handler that runs when the application starts.
    It creates all database tables.
    """
    from app.database import Base, engine
    Base.metadata.create_all(bind=engine)
