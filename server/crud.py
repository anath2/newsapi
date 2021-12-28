from re import S
from typing import List, Optional

from . import schema, model
from sqlalchemy.orm import Session


def create_country(conn: Session, country: schema.CountryCreate) -> model.Country:
    db_country = model.Country(**country.dict())
    conn.add(db_country)
    conn.commit()
    conn.refresh(db_country)
    return db_country


def create_news(conn: Session, country_id: int, news: schema.NewsCreate) -> model.News:
    db_news = model.News(**news.dict(), country_id=country_id)
    conn.add(db_news)
    conn.commit()
    conn.refresh(db_news)
    return db_news


def read_country(conn: Session, country_id: int) -> Optional[model.Country]:
    return conn.query(model.Country).filter(model.Country.id == country_id).first()


def read_country_by_iso(conn: Session, iso: str) -> Optional[model.Country]:
    return conn.query(model.Country).filter(model.Country.iso == iso).first()


def read_news(conn: Session, news_id: int) -> Optional[model.News]:
    return conn.query(model.News).filter(model.News.id == news_id).first()


def read_news_by_country(conn: Session, country_id: int) -> Optional[List[model.News]]:
    country = conn.query(model.Country).filter(model.Country.id == country_id).first()
    return country.news


def read_news_by_headline(conn: Session, headline: str) -> Optional[model.News]:
    return conn.query(model.News).filter(model.News.headline == headline).first()
