import logging
from db.checkdb import check_db_exists
from db.createdb import create_db
from db.conn import connection, close_conn
from psycopg import Error
from decouple import config
from db.checktable import check_tables
from db.createtables import create_table


def main():
    """Función principal que comprueba la existencia de una base de datos y crea las tablas si es necesario."""
    conn = connection(config("DB_NAME"))  # Establece la conexión a la base de datos
    if conn is None:
        return

    try:
        # Verifica si la base de datos existe
        if not check_db_exists():
            logging.info("La base de datos no existe. Creando nueva base de datos...")
            create_db()  # Crea la base de datos
        else:
            logging.info(f"{config('DB_NAME')} ya existe.")

        # Verifica la existencia de las tablas y las crea si es necesario
        table_names = config("TABLE_NAMES").split(",")

        for table_name in table_names:
            table_existence = check_tables(table_name)
            if table_existence:
                logging.info(f"La tabla {table_name} existe en la base de datos {config('DB_NAME')}.")
            else:
                logging.info(f"La tabla {table_name} no existe en la base de datos {config('DB_NAME')}. Creando...")
                create_table(config("DB_NAME"), table_name)
                logging.info(f"Tabla {table_name} creada exitosamente.")

    except Error as e:
        logging.error(f"Se produjo un error: {e}")
    finally:
        close_conn(conn)  # Cierra la conexión a la base de datos


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
