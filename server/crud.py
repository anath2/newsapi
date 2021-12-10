from  typing import Optional
from . import schema, model, db


def create_country(conn: d, country: schema.Country) -> model.Country:
    db_country = model.Country(**country.as_dict())
    conn.add(db_country)
    conn.commit()
    conn.refresh(db_country)
    return db_country
    

def read_country(conn, country_id):
    return conn.query(model.Country).filter(id=country_id).first()


def read_article_data(conn, article_id) -> Optional[model.Article]:
    return conn.query(Model.Article).filter(id=article_id).first()


def create_article(conn, article, country_id):
    db_article = model.Article(**article.as_dict(), country_id=country_id)
    conn.add(db_article)    
    conn.commit()
    conn.refresh(db_article)
    return db_article

