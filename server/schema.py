from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from pydantic.errors import DecimalIsNotFiniteError


class NewsDetail(BaseModel):
    id: int
    url: str
    headline: str
    description: str
    sentiment: Optional[int]
    ml_summary: Optional[str]


class NewsSummary(BaseModel):
    id: int
    url: str
    headline: str
    sentiment: Optional[int]


class Country(BaseModel):
    id: int
    iso: str
    num_stories: int
    last_updated_on: datetime

