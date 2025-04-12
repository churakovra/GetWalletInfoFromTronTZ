from pydantic import BaseModel
from decimal import Decimal


class WalletResponse(BaseModel):
    wallet_addr: str
    bandwidth: int
    account_energy: int | str
    account_balance: Decimal
