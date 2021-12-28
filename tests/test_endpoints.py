"""
Available endpoints:
    /country
    /news
    /news/{news_id}
"""

import pytest
from datetime import datetime
from server import app
from httpx import AsyncClient


@pytest.mark.asyncio
@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def country():
    # FastAPI uses iso for datetime input
    last_updated_on = datetime.utcnow().isoformat()
    return {"iso": "hk", "last_updated_on": last_updated_on}


@pytest.fixture
def news():
    return {
        "url": "http://someurl.com",
        "headline": "Test headline",
        "description": "Test Description",
    }


@pytest.mark.asyncio
async def test_crud(client, country, news):
    # Country crud
    rsp = await client.post("/country", json=country)
    assert rsp.status_code == 200

    cid = rsp.json()["id"]
    rsp = await client.get(f"/country/{cid}")
    assert rsp.status_code == 200

    # News crud
    rsp = await client.post(f"/country/{cid}/news", json=news)
    assert rsp.status_code == 200

    rsp = await client.get(f"/country/{cid}/news")
    assert rsp.status_code == 200

    first = rsp.json()[0]
    nid = first["id"]
    rsp = await client.get(f"/news/{nid}")
    assert rsp.status_code == 200
