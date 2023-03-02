"""Handler."""
import httpx

from .schemas.response import WebhookResponse


class RequestHandler:
    """HTTP request handler.

    ref: https://stackoverflow.com/a/74397436
    """

    @staticmethod
    async def call_external_api(
        client: httpx.AsyncClient,
        url: str,
        method: str,
        *args,
        **kwargs
    ) -> WebhookResponse:
        """Make a request to an external API."""
        if method == "GET":
            resp = await client.get(url, *args, **kwargs)
        elif method == "POST":
            resp = await client.post(url, *args, **kwargs)
        return WebhookResponse(
            url=url,
            status_code=resp.status_code,
            body=resp.text,
            headers=resp.headers,
        )
