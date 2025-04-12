import requests
from tronpy import Tron
from tronpy.providers import HTTPProvider

from app.config.preferences import API_KEY, BAD_AMOUNT_MESSAGE, BAD_AMOUNT
from app.models.WalletModel import Wallet
from app.models.WalletResponseModel import WalletResponse

client = Tron(
    provider=HTTPProvider(
        api_key=API_KEY
    )
)


async def get_wallet_data_from_tron(wallet: Wallet) -> WalletResponse | None:
    bandwidth = client.get_bandwidth(wallet.address)
    account_balance = client.get_account_balance(wallet.address)
    account_energy = await get_account_energy(wallet)
    response = WalletResponse(
        wallet_addr=wallet.address,
        bandwidth=bandwidth,
        account_energy=account_energy if account_energy > 0 else BAD_AMOUNT_MESSAGE,
        account_balance=account_balance
    )
    return response


async def get_account_energy(wallet: Wallet) -> int:
    account = client.get_account(wallet.address)
    account_frozen_v2 = account["frozenV2"]
    energy_weight = -1
    try:
        for item in account_frozen_v2:
            if item.get("amount"):
                energy_weight = item.get("amount")
            else:
                energy_weight = BAD_AMOUNT
    except Exception:
        print(Exception)
        energy_weight = BAD_AMOUNT
    finally:
        if energy_weight == BAD_AMOUNT:
            return energy_weight

    account_resources = client.get_account_resource(wallet.address)
    total_energy_limit = account_resources["TotalEnergyLimit"]
    total_energy_weight = account_resources["TotalEnergyWeight"]

    account_energy = int((energy_weight / total_energy_weight) * total_energy_limit)
    return account_energy
