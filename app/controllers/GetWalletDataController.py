from fastapi import APIRouter

getWalletDataRouter = APIRouter()


@getWalletDataRouter.post("/wallet/{wallet_adr}")
async def get_wallet_data(wallet: Wallet):
    pass
