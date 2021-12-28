import os
from . import constants as c
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


env = os.environ.get("ENV")


if env is None or env.strip().lower() != "testing":
    url = c.SQLALCHEMY_DATABASE_URL
else:
    url = c.SQLALCHEMY_DATABASE_TEST_URL

Base = declarative_base()
engine = create_engine(url, echo=True, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
