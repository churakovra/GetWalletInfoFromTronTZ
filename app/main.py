from fastapi import FastAPI

from app.controllers.GetQueryHistoryController import get_query_history_router
from app.controllers.GetWalletDataController import get_wallet_data_router
from app.controllers.RootController import root_router

app = FastAPI()

app.include_router(root_router)
app.include_router(get_wallet_data_router)
app.include_router(get_query_history_router)
