from pydantic import BaseModel

from app.models.WalletLogModel import WalletLog


class HistoryWallets(BaseModel):
    response: dict[str:WalletLog]
