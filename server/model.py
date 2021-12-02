from sqlalchemy.sql.elements import CollationClause
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Integer
from .db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relation, relationship


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(128), nullable=False)
    headline = Column(String(512), nullable=False)
    sentiment = Column(Integer)
    ml_summary = Column(String)
    description = Column(String)

    country = relationship("Country", back_populates="articles")
    country_id = Column(Integer, ForeignKey("country.id"))


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    iso = Column(String(2), nullable=False)
    last_updated_on = Column(DateTime, nullable=False)
    articles = relationship("Article", back_populates="country")

