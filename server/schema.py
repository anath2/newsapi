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

    class Config:
        orm = True


class NewsSummary(BaseModel):
    id: int
    url: str
    headline: str
    sentiment: Optional[int]

    class Config:
        orm = True


class Country(BaseModel):
    id: int
    iso: str
    num_stories: int
    last_updated_on: datetime

    class Config:
        orm = True

