from .conn import connection
from psycopg import OperationalError
import logging
from decouple import config


def create_db():
    """ Crea una base de datos con un nombre dado """
    conn = connection(db_name="postgres")
    dbname = config("DB_NAME")
    createdb = f"""CREATE DATABASE {dbname};"""
    try:
        with conn.cursor() as cur:
            cur.execute(createdb)
            conn.commit()
            print(f"Database {dbname} has been created")
    except OperationalError as oe:
        logging.info(f"Operational error occurred while creating database:\n{oe}")
    finally:
        if conn is not None:
            conn.close()
