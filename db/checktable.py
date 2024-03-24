from db.conn import connection
from psycopg import Error
from decouple import config
import json
import logging


def check_tables(db_name):
    conn = connection(db_name)
    if conn is None:
        return False

    try:
        table_names = config("TABLE_NAMES").split(",")
        #table_names = json.loads(table_names_json)  # Convertir la cadena JSON a lista de python
        logging.info("Ejecutando consulta para la tabla: %s", table_names)
        with conn.cursor() as curr:
            for table_name in table_names:
                # Ejecuta una consulta SQL para verificar la existencia de la tabla
                logging.info("Ejecutando consulta para la tabla: %s", table_name)
                curr.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
                exists = curr.fetchone()[0]
                if not exists:
                    logging.warning("la tabla %s no existe", table_name)
                    return False
                else:
                    logging.info("la tabla %s existe", table_name)
            return True  # Si todas las tablas existen, retorna True después del bucle
    except json.JSONDecodeError as je:
        logging.error("Error al cargar la cadena Json: %s", je)
        return False
    except Error as e:
        print("Error al ejecutar la consulta SQL", e)
        return False
    finally:
        if conn is not None:
            conn.close()
