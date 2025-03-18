from fastapi import FastAPI, WebSocket, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from .models.crypto import Base, get_db, engine
from .endpoints.crypto import router as crypto_router

app = FastAPI(title="Crypto Monitor")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Создание таблиц в базе данных
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

# Подключение WebSocket
@app.websocket("/ws/price")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Здесь будет логика обновления данных

app.include_router(crypto_router, prefix="/api")