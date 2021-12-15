import os
from . import constants as c
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if os.environ.get("API_ENV").lower().strip() == "testing":
    url = c.SQLALCHEMY_DATABASE_TEST_URL
else:
    url = c.SQLALCHEMY_DATABASE_URL

Base = declarative_base()
engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
