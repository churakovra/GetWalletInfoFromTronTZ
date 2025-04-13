import pytest_asyncio
from httpx import AsyncClient


@pytest_asyncio.fixture
async def async_http_client():
    async with AsyncClient(base_url="http://0.0.0.0") as client:
        yield client
