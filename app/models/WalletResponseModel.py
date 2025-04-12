from pydantic import BaseModel
from decimal import Decimal

from app.models.WalletModel import Wallet


class WalletResponse(BaseModel):
    wallet_addr: Wallet.address
    bandwidth: int
    account_energy: int
    account_balance: Decimal
