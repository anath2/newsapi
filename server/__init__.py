# TODO
# - Add support for background task status
# - Add support for storing downloaded data in global variable accessible across app

__version__ = "0.1.0"

from typing import List
from dotenv import load_dotenv
from aiohttp import ClientSession
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks

from . import schema, core
from .db import SessionLocal, crud


load_dotenv()
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/country", response_model=schema.Country)
async def create_country(country: schema.CountryCreate, db: Session = Depends(get_db)):
    iso = country.iso
    db_country = crud.read_country_by_iso(db, iso)
    if db_country:
        raise HTTPException(status_code=400, detail="Country already exists")
    created = crud.create_country(db, country)
    return created


@app.get("/country/{id}", response_model=schema.Country)
async def get_country_detail(id: int, db: Session = Depends(get_db)):
    db_country = crud.read_country(db, id)
    if not db_country:
        raise HTTPException(status_code=404, detail="No data for country")
    return db_country


@app.post("/country/{country_id}/news", response_model=schema.News)
async def create_news(
    country_id: int, news: schema.NewsCreate, db: Session = Depends(get_db)
):
    headline = news.headline
    db_news = crud.read_news_by_headline(db, headline)
    if db_news:
        raise HTTPException(status_code=400, detail="News article already exists")
    return crud.create_news(db, country_id, news)


@app.get("/country/{country_id}/news", response_model=List[schema.News])
async def get_country_news(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.read_country(db, country_id)
    if not db_country:
        raise HTTPException(status_code=404, detail="No news articles for country")
    result = crud.read_news_by_country(db, country_id)
    return result if result is not None else []


@app.get("/news/{id}", response_model=schema.News)
async def get_article(id, db: Session = Depends(get_db)):
    db_news = crud.read_news(db, id)
    if not db_news:
        raise HTTPException(status_code=404, detail="News article not found")
    return db_news


@app.post("/news/download")
async def start_news_download(
    news_list: List[schema.NewsCreate], background_tasks: BackgroundTasks
):
    background_tasks.add_task(_download_news, news_list)


async def _download_news(news_list: List[schema.NewsCreate]) -> List[schema.NewsCreate]:
    result = []
    async with ClientSession() as sess:
        for n in news_list:
            txt = await core.fetch_text(n.url, sess)
            # TODO Update this
            n_ = n.copy()
            n_.text = txt
            result.append(txt)

    return result
