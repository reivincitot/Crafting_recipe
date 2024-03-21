import psycopg as ps
from decouple import config
from psycopg import OperationalError, ProgrammingError
import logging


def connection(db_name):
    try:
        conn = ps.connect(
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            host=config("DB_HOST"),
            dbname=db_name
        )
        conn.autocommit = True  # Establece autocomit en True para la creación de la base de datos
        return conn
    except OperationalError as oe:
        logging.info(f"El error {oe} se ha encontrado al momento de conectarse a la base de datos")
        return None


def close_conn(conn):
    try:
        if conn is not None and conn.open is False:
            conn.close()
    except (OperationalError, ProgrammingError) as er:
        print(f"Error closing the connection: {er}")
