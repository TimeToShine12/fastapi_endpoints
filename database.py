from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


USER_NAME = os.environ["USER_NAME"],
USER_PASSWORD = os.environ["USER_PASSWORD"],
USER_HOST = os.environ["USER_HOST"],
USER_PORT = os.environ["USER_PORT"],
USER_DATABASE = os.environ["USER_DATABASE"]

SQLALCHEMY_DATABASE_URL = "postgresql://%(USER_NAME)s:%(USER_PASSWORD)s@%(USER_HOST)s:%(USER_PORT)s/%(USER_DATABASE)s"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
