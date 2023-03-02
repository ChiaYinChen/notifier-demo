"""Schema for response."""
from typing import Any

from pydantic import BaseModel


class Message(BaseModel):
    """Message output."""
    message: Any


class WebhookResponse:
    """A wrapper for the webhook response."""

    def __init__(
        self,
        *,
        url: str,
        status_code: int,
        body: str,
        headers: dict,
    ):
        self.api_url = url
        self.status_code = status_code
        self.body = body
        self.headers = headers
