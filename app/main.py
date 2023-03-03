"""Main app."""
from fastapi import FastAPI

from .routers import index, slack

app = FastAPI()
app.include_router(index.router)
app.include_router(slack.router, prefix="/api/slack", tags=["slack"])
