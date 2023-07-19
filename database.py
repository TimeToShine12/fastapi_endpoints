from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.USER_NAME}:{settings.USER_PASSWORD}@{settings.USER_HOST}:{settings.USER_PORT}/{settings.USER_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
