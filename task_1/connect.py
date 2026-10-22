import psycopg
from contextlib import contextmanager
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER_NAME = os.getenv("POSTGRESS_DB_USER_NAME")
DB_USER_PASS = os.getenv("POSTGRESS_DB_USER_PASS")
DATABASE_URL = f"postgresql://{DB_USER_NAME}:{DB_USER_PASS}@localhost:5432/hw_db"

@contextmanager
def create_connection():
    connection = psycopg.connect(DATABASE_URL)

    yield connection

    connection.rollback()
    connection.close()
