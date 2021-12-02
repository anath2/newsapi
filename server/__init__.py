__version__ = '0.1.0'

import os
import aiohttp
import asyncio

from . import model
from typing import Dict
from fastapi import FastAPI
from dotenv import load_dotenv
from .constants import COUNTRIES


load_dotenv()
app = FastAPI()


@app.get('/country-data')
async def get_country_data(response_model=model.Country):
    pass
    # countries = constants.COUNTRIES
    # urls = [construct_headlines_request(c) for c in countries]
    # async with aiohttp.ClientSession(raise_for_status=True) as sess:
    #     news_json = await fetch_all(sess, urls)
    #     result = parse_news_json(news_json)
    # return result

@app.get("/country-data/{id}")
async def get_country_detail(id):
    pass


@app.get("/articles/{id}")
async def get_article(id):
    pass


async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch_one(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    results = [r for r in results if r is not None]
    return results


async def fetch_one(session, url: str):
    try:
        async with session.get(url) as rsp:
            data = await rsp.json()
            return data
    except Exception:
        return None

def construct_headlines_request(country: str):
    api_key = os.environ['API_KEY']
    return f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'


def parse_news_json(news_json: Dict) -> Dict:
    pass