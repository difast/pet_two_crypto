from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"
    
    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, server_default='now()')

# Подключение к базе данных
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()