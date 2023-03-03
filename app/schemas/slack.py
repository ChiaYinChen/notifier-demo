"""Schema for Slack."""
from pydantic import BaseModel


class SlackPayload(BaseModel):
    """Slack payload."""
    text: str
