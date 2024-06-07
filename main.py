from fastapi import FastAPI
from app.routers import auth, posts
from starlette.datastructures import Headers
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

class BodyLimiter:
    def __init__(self, app: ASGIApp, max_size: int) -> None:
        self.app = app
        self.max_size = max_size

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request = Request(scope, receive)
        headers = Headers(scope=scope)
        content_length = headers.get("content-length")

        if content_length:
            content_length = int(content_length)
            if content_length > self.max_size:
                response = JSONResponse({"detail": "Payload size exceeds the limit of 1 MB"}, status_code=413)
                await response(scope, receive, send)
                return

        await self.app(scope, receive, send)

app = FastAPI()

# Add BodyLimiter middleware
app.add_middleware(BodyLimiter, max_size=1_048_576)  # 1 MB in bytes

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