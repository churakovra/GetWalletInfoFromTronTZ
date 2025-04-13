import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

ENERGY_URL_BODY = "https://api.shasta.trongrid.io/wallet/validateaddress"

WALLET_DB_USER = os.getenv("WALLET_DB_USER")
WALLET_DB_PASSWORD = os.getenv("WALLET_DB_PASSWORD")
HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")
PORT = os.getenv("PORT")

DATABASE_URL = f"postgresql://{WALLET_DB_USER}:{WALLET_DB_PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

BAD_AMOUNT = -100
BAD_AMOUNT_MESSAGE = "NO DATA ABOUT AMOUNT"