from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from app.controllers.GetQueryHistoryDBConroller import get_query_history_from_db
from app.database import get_db
from app.models.HistoryWalletsModel import HistoryWallets

get_query_history_router = APIRouter()


@get_query_history_router.get("/last", response_model=HistoryWallets)
async def get_query_history(
        page: int = Query(default=1, ge=1),
        size: int = Query(10, ge=1, le=100),
        db: Session = Depends(get_db)
) -> HistoryWallets:
    response = await get_query_history_from_db(page, size, db)
    return response
