# backend/services/yt_service.py

from YouTubeMusic.Search import Search
from YouTubeMusic.Video_Stream import get_video_audio_urls
from utils.cache import get_cache, set_cache

async def search_youtube(query: str):
    cache_key = f"search:{query}"
    cached = get_cache(cache_key)
    if cached:
        return cached

    data = await Search(query, limit=10)

    results = []
    for r in data["main_results"]:
        results.append({
            "url": r["url"],   # FULL URL ONLY
            "title": r["title"],
            "channel": r["channel"],
            "duration": r["duration"],
            "views": r["views"],
            "thumbnail": r["thumbnail"]
        })

    set_cache(cache_key, results)
    return results


# 🔥 DIRECT URL — NO ID EXTRACTION
def get_stream_urls(url: str):
    return get_video_audio_urls(url)
