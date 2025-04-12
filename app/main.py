from fastapi import FastAPI, Depends

from app.controllers.GetQueryHistoryController import getQueryHistoryRouter
from app.controllers.GetWalletDataController import getWalletDataRouter
from app.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

app.include_router(getWalletDataRouter, prefix="/wallet/{wallet_adr}", dependencies=[Depends(get_db)])
app.include_router(getQueryHistoryRouter, prefix="/last", dependencies=[Depends(get_db)])
