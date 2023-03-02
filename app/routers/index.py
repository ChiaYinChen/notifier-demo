"""Index endpoint."""
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/", include_in_schema=False)
async def main():
    return RedirectResponse(url="/docs")
