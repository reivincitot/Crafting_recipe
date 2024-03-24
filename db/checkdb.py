from .conn import connection
from decouple import config
from psycopg import OperationalError, ProgrammingError
import logging


def check_db_exists():
    """
     Verifica si la base de datos especificada en el archivo de configuración existe en el servidor de bases de datos.

     Returns:
     - bool: True si la base de datos existe, False si no existe o si ocurre algún error.
     """
    dbname = config("DB_NAME")
    conn = connection(db_name=dbname)
    if conn is None:
        logging.error("Error: No se pudo conectar a la base de datos.")
        return False

    try:
        with conn.cursor() as cur:
            cur.execute("""SELECT 1 FROM pg_database WHERE datname= %s """, (dbname,))
            exists = cur.fetchone()
            if exists is not None:
                print(f"La base de datos '{dbname}' existe en el servidor PostgreSQL.")
                return True
            else:
                print(f"La base de datos '{dbname}' no existe en el servidor PostgreSQL.")
                return False
    except OperationalError as oe:
        logging.error(f"Error de operación al verificar la existencia de la base de datos: {oe}")
        return False
    except ProgrammingError as pe:
        logging.error(f"Error de programación al verificar la existencia de la base de datos: {pe}")
        return False
    finally:
        if conn is not None:
            conn.close()
