import httpx
import os
from datetime import datetime

COIN_GECKO_URL = os.getenv("COIN_GECKO_URL")

async def fetch_crypto_price(coin_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{COIN_GECKO_URL}/simple/price?ids={coin_id}&vs_currencies=usd"
        )
        return {
            "coin_id": coin_id,
            "price": response.json()[coin_id]["usd"],
            "timestamp": datetime.now()
        }