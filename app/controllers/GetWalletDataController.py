from fastapi import APIRouter, Request, Depends

from app.controllers.LogWalletDBController import wallet_db_log
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.WalletModel import Wallet
from app.models.WalletResponseModel import WalletResponse

from app.controllers.TronController import get_wallet_data_from_tron

get_wallet_data_router = APIRouter()


@get_wallet_data_router.post("/wallet", response_model=WalletResponse)
async def get_wallet_data(wallet: Wallet, request: Request, db: Session = Depends(get_db)):
    response = await get_wallet_data_from_tron(wallet)
    await wallet_db_log(wallet, request.client.host, db)
    return response

