from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class NewsBase(BaseModel):
    url: str
    headline: str
    description: str


class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int

    class Config:
        orm = True


class NewsSummary(NewsBase):
    sentiment: Optional[int]


class NewsDetail(NewsBase):
    sentiment: Optional[int]
    ml_summary: Optional[str]


class CountryBase(BaseModel):
    iso: str
    last_updated_on: datetime


class CountryCreate(CountryBase):
    pass


class Country(BaseModel):
    id: int

    class Config:
        orm = True
