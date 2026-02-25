from fastapi import FastAPI
from routes import search, watch, suggest, auth, user, trending

app = FastAPI(title="AbhiTube Pro")

app.include_router(search.router, prefix="/api/search")
app.include_router(watch.router, prefix="/api/watch")
app.include_router(suggest.router, prefix="/api/suggest")
app.include_router(auth.router, prefix="/api/auth")
app.include_router(user.router, prefix="/api/user")
app.include_router(trending.router, prefix="/api/trending")
