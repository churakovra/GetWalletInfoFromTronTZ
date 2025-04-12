from pydantic import BaseModel


class WalletResponse(BaseModel):
    response: dict[str:str]
