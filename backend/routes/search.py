from fastapi import APIRouter
from services.yt_service import search_youtube

router = APIRouter()

@router.get("/")
async def search(q: str):
    return await search_youtube(q)
