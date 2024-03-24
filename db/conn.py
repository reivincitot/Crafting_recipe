import psycopg as ps
from decouple import config
import logging


def connection(db_name):
    """
       Establece una conexión a la base de datos utilizando los valores del archivo .env.

       Args:
       - db_name (str): El nombre de la base de datos a la que se desea conectar.

       Returns:
       - conn (psycopg.connection): La conexión establecida, o None si la conexión falla.
       """
    try:
        dbname = db_name or config("DB_NAME")
        conn = ps.connect(
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            host=config("DB_HOST"),
            dbname=dbname
        )
        conn.autocommit = True  # Establece autocommit en True para la creación de la base de datos
        return conn
    except ps.OperationalError as oe:
        logging.info(f"El error al conectarse a la base de datos: {oe}")
        return None
    except Exception as e:
        logging.error(f"Error al conectar a la base de datos: {e}")
        return None


def close_conn(conn):
    """
    Cierra la conexión a la base de datos, si está abierta.

    Args:
    - conn (psycopg.connection): La conexión que se desea cerrar.
    """
    try:
        if conn is not None and not conn.close:
            conn.close()
    except Exception as er:
        logging.error(f"Error cerrando la conexión: {er}")
