from datetime import datetime

from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.WalletLogModelDB import WalletLog
from app.models.WalletModel import Wallet


async def wallet_db_log(wallet: Wallet, user_host: str, db: Session = Depends()):
    current_dt = datetime.now()
    wallet_log = WalletLog(
        wallet_address=wallet.address,
        query_datetime=current_dt,
        query_user=user_host
    )
    db.add(wallet_log)
    db.commit()
    db.refresh(wallet_log)
    return wallet_log
