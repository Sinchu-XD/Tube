from fastapi import APIRouter
from backend.database import history

router = APIRouter()

@router.get("/")
async def trending():
    pipeline = [
        {"$group": {"_id": "$url", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    return list(history.aggregate(pipeline))
