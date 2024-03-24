import logging
from psycopg import OperationalError
from db.querys import table_query
from db.checktable import check_tables
from db.conn import connection


def create_table(db_name, table_name):
    conn = connection(db_name)
    if conn is None:
        return False

    try:
        with conn.cursor() as curr:
            if not check_tables(table_name):
                query = table_query.get(table_name)
                if query:
                    curr.execute(query)
                    logging.info(f"Tabla {table_name} creada exitosamente.")
                    conn.commit()
                    return True
                else:
                    logging.error(f"No se encontró la consulta para la tabla {table_name}")
            else:
                logging.info(f"La tabla {table_name} ya existe en la base de datos.")
                return True

    except OperationalError as oe:
        logging.error(f"Un error ha ocurrido: {oe}")

    finally:
        try:
            if conn is not None:
                conn.close()
        except Exception as e:
            logging.error(f"Error al cerrar la conexión: {e}")
