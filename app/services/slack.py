"""Slack Services."""
import httpx

from ..config import settings
from ..handler import RequestHandler
from ..schemas.response import WebhookResponse


class SlackService:
    """Send notification on Slack using Webhook."""

    webhook_url = settings.SLACK_WEBHOOK_URL

    @classmethod
    async def send(
        cls, client: httpx.AsyncClient, text: str
    ) -> WebhookResponse:
        """Send message."""
        return await RequestHandler.call_external_api(
            client=client,
            url=cls.webhook_url,
            method="POST",
            headers={"Content-type": "application/json"},
            json={
                "text": text,
                "username": settings.SLACK_USERNAME,
                "icon_emoji": settings.SLACK_ICON_EMOJI
            }
        )
