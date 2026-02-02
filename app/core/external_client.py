import httpx

FAKE_API_KEY = "secret-api-key"
BASE_URL = "http://127.0.0.1:8000/external-api"


async def fetch_external_status():
    headers = {"X-API-Key": FAKE_API_KEY}

    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.get(f"{BASE_URL}/status", headers=headers)
        response.raise_for_status()
        return response.json()
