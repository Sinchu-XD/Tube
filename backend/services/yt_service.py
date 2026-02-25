from YouTubeMusic.Search import Search
from YouTubeMusic.Video_Stream import get_video_audio_urls
from utils.helpers import extract_video_id
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
            "url": r["url"],
            "title": r["title"],
            "channel": r["channel"],
            "duration": r["duration"],
            "views": r["views"],
            "thumbnail": r["thumbnail"]
        })

    set_cache(cache_key, results)
    return results


def get_stream_urls(url: str):
    video_id = extract_video_id(url)
    if not video_id:
        return None, None

    link = f"https://youtube.com/watch?v={video_id}"
    return get_video_audio_urls(link)
