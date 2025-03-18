from celery import Celery
from api.services.coin_gecko import fetch_crypto_price
import os

celery = Celery(
    __name__,
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("REDIS_URL")
)

@celery.task
async def update_crypto_prices(coin_id: str):
    data = await fetch_crypto_price(coin_id)
    # Здесь будет сохранение в базу данных
    return data