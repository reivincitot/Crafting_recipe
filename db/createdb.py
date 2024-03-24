from .conn import connection
from psycopg import OperationalError, ProgrammingError
import logging
from decouple import config


def create_db():
    """
    Crea una base de datos con el nombre especificado en el archivo de configuración.

    Returns:
    - bool: True si la base de datos se creó correctamente, False si ocurrió algún error.
    """
    conn = connection(db_name="postgres")
    dbname = config("DB_NAME")
    createdb = f"""CREATE DATABASE {dbname};"""
    try:
        with conn.cursor() as cur:
            cur.execute(createdb)
            conn.commit()
            logging.info(f"Database {dbname} has been created successfully.")
            return True
    except (OperationalError, ProgrammingError) as e:
        logging.error(f"Error occurred while creating database:{e}")
        return False
    finally:
        if conn is not None:
            conn.close()
