from pymongo import MongoClient
from backend.config import MONGO_URL, DB_NAME

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

users = db["users"]
history = db["history"]
