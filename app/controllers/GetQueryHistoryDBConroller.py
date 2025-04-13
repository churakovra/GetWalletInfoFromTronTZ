from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.HistoryWalletsModel import HistoryWallets
from app.models.WalletLogModel import WalletLog
from app.models.WalletLogModelDB import WalletLogDB as WalletLogDB
from app.models.WalletModel import Wallet


async def get_query_history_from_db(
        page: int,
        size: int,
        db: Session
) -> HistoryWallets:
    offset = (page - 1) * size
    stmt = select(WalletLogDB).offset(offset).limit(size)
    items = db.scalars(stmt).all()

    history_wallets = HistoryWallets()

    for item in items:
        history_wallets.response.append(
            WalletLog(
                wallet=Wallet(address=item.wallet_address),
                datetime=item.query_datetime,
                user=item.query_user
            )
        )

    return history_wallets
