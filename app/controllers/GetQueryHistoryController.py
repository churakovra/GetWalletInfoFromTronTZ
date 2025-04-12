from fastapi import APIRouter, Query

getQueryHistoryRouter = APIRouter()


@getQueryHistoryRouter.get("/last")
async def get_query_history(amount: int = Query(10, ge=1)):
    pass
