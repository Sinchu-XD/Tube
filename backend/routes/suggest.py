from fastapi import APIRouter
from services.suggestion_service import get_suggestions

router = APIRouter()

@router.get("/")
async def suggest(title: str, url: str):
    return await get_suggestions(title, url)
