import jwt
import bcrypt
from config import JWT_SECRET, JWT_ALGO

def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def create_token(data: dict):
    return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

def decode_token(token: str):
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
