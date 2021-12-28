from server.model import Base
from server.db import engine

Base.metadata.create_all(bind=engine)
