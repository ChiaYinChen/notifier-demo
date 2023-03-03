"""Slack endpoint."""
import httpx
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ..deps import get_client
from ..schemas.response import Message
from ..schemas.slack import SlackPayload
from ..services.slack import SlackService

router = APIRouter()


@router.post(
    "/send",
    response_model=Message,
)
async def send_message(
    slack_payload: SlackPayload,
    client: httpx.AsyncClient = Depends(get_client),
):
    """Send slack notification."""
    resp = await SlackService.send(client, slack_payload.text)
    if resp.status_code != 200:
        return JSONResponse(
            status_code=resp.status_code,
            content={"message": "Failed to send message to Slack"},
        )
    return Message(message=resp.body)
