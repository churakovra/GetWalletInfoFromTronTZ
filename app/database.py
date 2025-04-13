from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.preferences import DATABASE_URL
from app.models.WalletLogModelDB import Base

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

async def lifespan_init_db(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
