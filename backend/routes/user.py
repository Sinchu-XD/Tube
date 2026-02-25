from fastapi import APIRouter
from backend.database import history
from datetime import datetime

router = APIRouter()

@router.post("/history")
async def save_history(user: str, url: str):
    history.insert_one({
        "user": user,
        "url": url,
        "watched_at": datetime.utcnow()
    })
    return {"status": "saved"}

@router.get("/history/{user}")
async def get_history(user: str):
    return list(history.find({"user": user}, {"_id": 0}))
