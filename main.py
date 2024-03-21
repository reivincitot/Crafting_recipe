import logging
from db.checkdb import check_db_exists
from db.createdb import create_db
from db.conn import connection
from psycopg import Error
from decouple import config


def main():
    """ Función principal que comprueba la existencia de una base de datos y la crea de ser necesarios """
    conn = connection()
    check_db = check_db_exists()  # Verifica si la base de datos existe

    try:
        # Check if the database exists
        if not check_db:
            print("\nDatabase does not exist! Creating new database...\n")
            create_db()  # Crea la base de datos
        else:
            print(f"\n{config("DB_NAME")} already exists!\n")
    except Error as e:
        logging.info(f"Un error ha ocurrido:", e)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
