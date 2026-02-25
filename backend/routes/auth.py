from fastapi import APIRouter, HTTPException
from backend.database import users
from backend.utils.auth_utils import hash_password, verify_password, create_token

router = APIRouter()

@router.post("/register")
async def register(email: str, password: str):
    if users.find_one({"email": email}):
        raise HTTPException(400, "User already exists")

    users.insert_one({
        "email": email,
        "password": hash_password(password)
    })

    return {"status": "registered"}

@router.post("/login")
async def login(email: str, password: str):
    user = users.find_one({"email": email})

    if not user or not verify_password(password, user["password"]):
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"email": email})
    return {"token": token}
