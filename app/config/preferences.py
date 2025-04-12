import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
ENERGY_URL_BODY = "https://api.shasta.trongrid.io/wallet/validateaddress"