from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WalletLogDB(Base):
    __tablename__ = "wallets_log"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    wallet_address = Column(String, nullable=False)
    query_datetime = Column(DateTime, default=datetime.now)
    query_user = Column(String, nullable=False)
