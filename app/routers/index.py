"""Index endpoint."""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", include_in_schema=False)
async def main():
    html_content = """
    <html>
        <body>
            <a href="http://127.0.0.1:8000/docs">Go to API docs</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
