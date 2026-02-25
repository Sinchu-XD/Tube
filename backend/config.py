import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Vexera:Vexera@vexera.wtrsmyc.mongodb.net/?appName=Vexera")
REDIS_URL = os.getenv("REDIS_URL", "redis://default:AVgtAAIncDIyNjNlODI3MzNkZTc0ZTE1YmZjOTZkZmZiZDIxODk2MnAyMjI1NzM@accepted-woodcock-22573.upstash.io:6379")
DB_NAME = "abhitube"

JWT_SECRET = os.getenv("JWT_SECRET", "e43f42172ea2fbd677e498373ec0d425e3adcb6df2dc754118bc989a7e599482")
JWT_ALGO = "HS256"
