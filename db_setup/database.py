# database.py
from sqlalchemy import create_engine as sa_create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from configs.config import Configs
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DB_CONFIGS = Configs.get_database_configs('./config.toml')
DATABASE_URL = Configs.url_string_conn(DB_CONFIGS)

Base = declarative_base()

def create_db_engine(DATABASE_URL):
    logging.debug(DATABASE_URL)
    engine = sa_create_engine(DATABASE_URL, pool_size=10, max_overflow=20, pool_recycle=3600)
    return engine

def create_section(engine):
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return SessionLocal
