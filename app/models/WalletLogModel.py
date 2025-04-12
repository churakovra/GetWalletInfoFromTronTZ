from pydantic import BaseModel

from app.models.WalletModel import Wallet
from datetime import datetime


class WalletLog(BaseModel):
    wallet: Wallet
    datetime: datetime
    user: str
