from datetime import datetime

from sqlalchemy.orm import Session

from app.models.WalletLogModelDB import WalletLogDB
from app.models.WalletModel import Wallet


async def wallet_db_log(wallet: Wallet, user_host: str, db: Session) -> bool:
    current_dt = datetime.now()
    wallet_log = WalletLogDB(
        wallet_address=wallet.address,
        query_datetime=current_dt,
        query_user=user_host
    )
    try:
        db.add(wallet_log)
        db.commit()
        db.refresh(wallet_log)
    except Exception:
        return False
    return True
