from db_setup.database import create_db_engine, Base  # Ensure Base is imported
from models.log_model import LogEntry  # Import your model
from configs.config import Configs
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

DB_CONFIGS = Configs.get_database_configs('config.toml')

DATABASE_URL = Configs.url_string_conn(DB_CONFIGS)

logging.debug(DATABASE_URL)

engine = create_db_engine(DATABASE_URL)

logging.debug("Attempting to create tables...")
try:
    Base.metadata.create_all(bind=engine)
    logging.debug("Table creation code executed.")
except Exception as e:
    logging.error("Error creating database tables: %s", e)
