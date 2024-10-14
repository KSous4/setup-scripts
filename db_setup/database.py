# database.py
from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

Base = declarative_base()

def create_db_engine(DATABASE_URL):
    logging.debug(DATABASE_URL)
    engine = sa_create_engine(DATABASE_URL, pool_size=10, max_overflow=20, pool_recycle=3600)
    return engine

def create_section(engine):
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return SessionLocal
