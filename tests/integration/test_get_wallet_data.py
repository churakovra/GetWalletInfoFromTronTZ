import pytest
from httpx import ASGITransport
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_get_wallet_data_success():
    transport = ASGITransport(app=app)
    test_wallet = {"address": "THwyeoCMSXQq2aGDpXpSqo89VnTtFktGGp"}

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/wallet", json=test_wallet)

    assert response.status_code == 200
