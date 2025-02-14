from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = "postgresql://admin_user:m0vie_rec0d@db:5432/MOVIE_RECORD_DB"

Engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=False
)

Base = declarative_base()

session = Session(
  autocommit = False,
  autoflush = False,
  bind = Engine
)