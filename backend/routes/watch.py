# backend/routes/watch.py

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from backend.services.yt_service import get_stream_urls
from YouTubeMusic.Video_Stream import start_ffmpeg_merge
import asyncio

router = APIRouter()

@router.get("/")
async def watch(request: Request, url: str):

    # Direct URL pass
    video_url, audio_url = get_stream_urls(url)

    if not video_url:
        raise HTTPException(400, "Invalid YouTube URL")

    process = start_ffmpeg_merge(video_url, audio_url)

    async def generator():
        try:
            while True:
                if await request.is_disconnected():
                    break

                chunk = await asyncio.to_thread(
                    process.stdout.read, 1024 * 512
                )

                if not chunk:
                    break

                yield chunk
        finally:
            process.kill()
            process.wait()

    return StreamingResponse(generator(), media_type="video/mp4")
