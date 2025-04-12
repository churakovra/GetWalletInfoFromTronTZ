import requests
from tronpy import Tron
from tronpy.providers import HTTPProvider

from app.config.preferences import API_KEY, ENERGY_URL_BODY
from app.models.WalletModel import Wallet
from app.models.WalletResponseModel import WalletResponse

client = Tron(
    provider=HTTPProvider(
        api_key=API_KEY
    )
)


async def get_wallet_data_from_tron(wallet: Wallet) -> WalletResponse | None:
    if not validate_addr(wallet):
        return None
    bandwidth = client.get_bandwidth(wallet.address)
    account_balance = client.get_account_balance(wallet.address)
    account_energy = await get_account_energy(wallet)
    response = WalletResponse(
        wallet_addr=wallet.address,
        bandwidth=bandwidth,
        account_energy=account_energy,
        account_balance=account_balance
    )
    return response


async def get_account_energy(addr) -> int:
    account_frozen_v2 = client.get_account(addr)["frozenV2"]
    energy_weight = account_frozen_v2["amount"]

    account_resources = client.get_account_resource(addr)
    total_energy_limit = account_resources["TotalEnergyLimit"]
    total_energy_weight = account_resources["TotalEnergyWeight"]

    account_energy = int((energy_weight / total_energy_weight) * total_energy_limit)
    return account_energy


async def validate_addr(wallet: Wallet) -> bool:
    payload = {
        "address": wallet.address,
        "visible": True
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    response = requests.post(ENERGY_URL_BODY, json=payload, headers=headers)
    return response.json().get("result")
