from fastapi import APIRouter

from app.models.WalletModel import Wallet

getWalletDataRouter = APIRouter()


@getWalletDataRouter.post("/wallet/{wallet_adr}")
async def get_wallet_data(wallet: Wallet):
    pass
