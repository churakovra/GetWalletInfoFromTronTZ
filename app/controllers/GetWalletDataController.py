from http.client import HTTPException

from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from tronpy.exceptions import BadAddress

from app.config.preferences import BAD_ADDRESS_EXCEPTION_MESSAGE
from app.controllers.LogWalletDBController import wallet_db_log
from app.controllers.TronController import get_wallet_data_from_tron
from app.database import get_db
from app.models.WalletModel import Wallet
from app.models.WalletResponseModel import WalletResponse

get_wallet_data_router = APIRouter()


@get_wallet_data_router.post("/wallet", response_model=WalletResponse)
async def get_wallet_data(
        wallet: Wallet,
        request: Request,
        db: Session = Depends(get_db)
) -> WalletResponse:
    try:
        response = await get_wallet_data_from_tron(wallet)
    except BadAddress:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=BAD_ADDRESS_EXCEPTION_MESSAGE
        )
    await wallet_db_log(wallet, request.client.host, db)
    return response
