from typing import Optional
from . import schema, model
from sqlalchemy.orm import Session


def create_country(conn: Session, country: schema.CountryCreate) -> model.Country:
    db_country = model.Country(**country.as_dict())
    conn.add(db_country)
    conn.commit()
    conn.refresh(db_country)
    return db_country


def create_news(conn: Session, country_id: int, news: schema.NewsCreate) -> model.News:
    db_news = model.News(**news.as_dict(), country_id=country_id)
    conn.add(db_news)
    conn.commit()
    conn.refresh(db_news)
    return db_news


def read_country(conn, country_id) -> Optional[model.Country]:
    return conn.query(model.Country).filter(id=country_id).first()


def read_country_by_iso(conn, iso: str) -> Optional[model.Country]:
    return conn.query(model.Country).filter(iso=iso).first()


def read_news(conn, news_id) -> Optional[model.News]:
    return conn.query(model.News).filter(id=news_id).first()


def read_news_by_headline(conn, headline: str) -> Optional[model.News]:
    return conn.query(model.News).filter(headline=headline).first()
