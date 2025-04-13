from typing import List

from pydantic import BaseModel, Field

from app.models.WalletLogModel import WalletLog


class HistoryWallets(BaseModel):
    response: List[WalletLog] = Field(default_factory=list)
