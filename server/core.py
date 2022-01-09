from bs4 import BeautifulSoup
from aiohttp import ClientSession
from typing import Union, Dict, List


def scrape_text(page_content: str, select_tags=["p"]) -> str:
    soup = BeautifulSoup(page_content)
    content = soup.find_all(select_tags)
    content = "\n".join(t.text for t in content)
    return content


async def fetch_text(url: str, session: ClientSession) -> str:
    async with session.get(url, raise_for_status=True) as rsp:
        return await rsp.text()


async def fetch_json(url: str, session: ClientSession) -> Union[List, Dict]:
    async with session.get(url, raise_for_status=True) as rsp:
        return await rsp.json()
