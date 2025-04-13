from datetime import datetime
from unittest.mock import MagicMock

import pytest

from app.controllers.LogWalletDBController import wallet_db_log
from app.models.WalletLogModelDB import WalletLogDB
from app.models.WalletModel import Wallet


@pytest.mark.asyncio
async def test_wallet_db_log():
    test_wallet = Wallet(address="THwyeoCMSXQq2aGDpXpSqo89VnTtFktGGp")
    ip = "127.0.0.1"

    db = MagicMock()

    await wallet_db_log(test_wallet, ip, db)

    assert db.add.called
    assert db.commit.called
    assert db.refresh.called

    db.add.assert_called_once()
    called_obj = db.add.call_args[0][0]
    assert isinstance(called_obj, WalletLogDB)
    assert called_obj.wallet_address == test_wallet.address
    assert called_obj.query_user == ip
    assert isinstance(called_obj.query_datetime, datetime)
