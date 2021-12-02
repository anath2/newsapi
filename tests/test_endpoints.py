import pytest
from server import app
from httpx import AsyncClient


@pytest.mark.asyncio
@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_get_country_data(client):
    response = await client.get('/country-data')
    print(response.json())
    assert response


@pytest.mark.asyncio
async def test_get_country_detail(client, test_id=0):
    response = await client.get(f'/country-data/{test_id}')
    print(response.json())
    assert response


@pytest.mark.asyncio
async def test_get_article(client, test_id=0):
    response = await client.get(f'/articles/{test_id}')
    print(response.json())
    assert response

