from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from app.database import get_db

get_query_history_router = APIRouter()


@get_query_history_router.get("/last")
async def get_query_history(amount: int = Query(10, ge=1), db: Session = Depends(get_db)):
    pass
