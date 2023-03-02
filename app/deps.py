"""Dependencies."""
from typing import AsyncGenerator

import httpx


async def get_client() -> AsyncGenerator:
    """Create a new client for each request."""
    async with httpx.AsyncClient() as client:
        # yield the client to the endpoint function
        yield client
        # close the client when the request is done
