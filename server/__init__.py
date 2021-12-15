__version__ = "0.1.0"

from dotenv import load_dotenv
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

from . import schema, crud
from .db import SessionLocal


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
    return crud.create_country(db, country)


@app.post("/news", response_model=schema.News)
async def create_news(
    news: schema.NewsCreate, country_id: int, db: Session = Depends(get_db)
):
    headline = news.headline
    db_news = crud.read_news_by_headline(db, headline)
    if db_news:
        raise HTTPException(status_code=400, detail="News article already exists")
    return crud.create_news(db, country_id, news)


@app.get("/country/{id}", response_model=schema.Country)
async def get_country_detail(id: str, db: Session = Depends(get_db)):
    db_country = crud.read_country(db, id)
    if not db_country:
        raise HTTPException(status_code=404, detail="No data for country")
    return db_country


@app.get("/news/{id}", response_model=schema.News)
async def get_article(id, db: Session = Depends(get_db)):
    db_news = crud.read_news(db, id)
    if not db_news:
        raise HTTPException(status_code=404, detail="News article not found")
    return db_news
