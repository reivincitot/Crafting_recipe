from .conn import connection
from psycopg import Error, OperationalError, ProgrammingError
import logging


def create_db():
    conn = connection()
    createdb = """CREATE DATABASE crafting_recipe;"""
    try:
        with conn.cursor() as cur:
            cur.execute(createdb)
            conn.commit()
            print("Database has been created")
    except OperationalError as oe:
        logging.info(f"Operational error occurred while creating database:\n{oe}")
    except ProgrammingError as pe:
        logging.info(f"Programming error occurred while creating database:\n{pe}")
    except Error as e:
        logging.info(f"Error ocurred while creating database: \n{e}")
    finally:
        conn.close()