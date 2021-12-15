from .db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(128), nullable=False)
    headline = Column(String(512), nullable=False)
    description = Column(String)

    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="news")


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    iso = Column(String(2), nullable=False)
    last_updated_on = Column(DateTime, nullable=False)

    news = relationship("News", back_populates="country")
