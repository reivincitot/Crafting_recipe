from db.checkdb import check_db_exists
from db.createdb import create_db
from db.conn import connection


def main():
    conn = connection()
    check_db = check_db_exists()
    try:
        # Check if the database exists
        if check_db == False:
            print("\nDatabase does not exist! Creating new database...\n")
            return create_db()
        else:
            print(f"\n{check_db} already exists!\n")
            pass
    finally:
        conn.close()

if __name__ == "__main__":
    main()
