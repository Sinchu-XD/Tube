import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")
DB_NAME = "abhitube"

JWT_SECRET = os.getenv("JWT_SECRET", "SUPER_SECRET_CHANGE_THIS")
JWT_ALGO = "HS256"
