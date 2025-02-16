import httpx


async def fetch_rss_feed(feed_url: str):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(feed_url)
            response.raise_for_status()
            return response.content

    except httpx.RequestError as e:
        print(f"HTTP request error: {e}")

    except httpx.HTTPStatusError as e:
        print(f"HTTP status error: {e.response.status_code} - {e}")

    except Exception as e:
        print(f"Exception {e} occurred while fetching RSS feed")

    return None
