from pydantic import BaseModel
from decimal import Decimal

from app.models.WalletModel import Wallet


class WalletResponse(BaseModel):
    wallet_addr: str
    bandwidth: int
    account_energy: int | str
    account_balance: Decimal
