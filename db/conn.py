import psycopg as ps
from decouple import config
from psycopg import OperationalError, ProgrammingError
import logging


def connection():
    try:
        dbname = (config("DB_NAME"))
        conn = ps.connect(
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            host=config("DB_HOST"),
            dbname="postgres"
        )
        conn.autocommit = True  # Establece autocomit en True para la creación de la base de datos
        with conn.cursor() as curr:
            curr.execute(f"CREATE DATABASE {dbname}")
            print(f"La base de datos {dbname} ha sido creada exitosamente ")
    except OperationalError as oe:
        logging.info(f"El error {oe} se ha encontrado al momento de conectarse a la base de datos")
        return None


def close_conn(conn):
    try:
        if conn is not None and conn.open is False:
            conn.close()
    except (OperationalError, ProgrammingError) as er:
        print(f"Error closing the connection: {er}")
