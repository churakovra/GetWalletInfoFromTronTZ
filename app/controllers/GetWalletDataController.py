from fastapi import APIRouter, Request

from app.models.WalletModel import Wallet
from app.models.WalletResponseModel import WalletResponse

from app.controllers.TronController import get_wallet_data_from_tron

getWalletDataRouter = APIRouter()


@getWalletDataRouter.post("/wallet/{wallet_adr}", response_model=WalletResponse)
async def get_wallet_data(wallet: Wallet, request: Request):
    response = get_wallet_data_from_tron(wallet)
    wallet_db_log(wallet, request.client.host)
    return response

