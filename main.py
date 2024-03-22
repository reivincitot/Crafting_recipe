import logging
from db.checkdb import check_db_exists
from db.createdb import create_db
from db.conn import connection
from psycopg import Error
from decouple import config
from db.checktable import check_tables
from db.createtables import create_table


def main():
    """ Función principal que comprueba la existencia de una base de datos y la crea de ser necesarios """
    conn = connection(config("DB_NAME"))  # Proporciona el nombre de la base de datos
    check_db = check_db_exists()  # Verifica si la base de datos existe
    table_names = ["juego"]

    try:
        # Check if the database exists
        if not check_db:
            print("\nDatabase does not exist! Creating new database...\n")
            create_db()  # Crea la base de datos
        else:
            print(f"\n{config("DB_NAME")} already exists!\n")

        for table_name in table_names:
            table_existence = check_tables(table_name, config("DB_NAME"))
            if table_existence:
                print(f"La tabla {table_name} existe en la base de datos {config("DB_NAME")}.")
            else:
                print(f"La Tabla {table_name} no existe en la base de datos {config("DB_NAME")}")
                create_table(config("DB_NAME"), table_name)
                print(f"Tabla {table_name} creada exitosamente")

    except Error as e:
        logging.info(f"Un error ha ocurrido:", e)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
