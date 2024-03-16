from db.checkdb import check_db_exists
from db.createdb import create_db
from db.conn import connection
from decouple import config


def main():
    """ Función principal que comprueba la existencia de una base de datos y la crea de ser necesarios """
    conn = connection()
    check_db = check_db_exists()
    dbname=config("DB_NAME")
    
    try:
        # Check if the database exists
        if not check_db_exists():
            print("\nDatabase does not exist! Creating new database...\n")
            create_db(db_name)
        else:
            print(f"\n{db_name} already exists!\n")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
