from pydantic import BaseModel
from typing import Dict

from app.models.WalletLogModel import WalletLog


class HistoryWallets(BaseModel):
    response: Dict[str:WalletLog]
