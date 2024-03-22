from psycopg import OperationalError

from db.checktable import check_tables
from db.conn import connection


def create_table(db_name, table_name):
    conn = connection(db_name)
    if conn is None:
        return False
    try:
        with conn.cursor() as curr:
            if not check_tables("game", db_name):
                curr.execute("""CREATE TABLE game (
                game_id SERIAL PRIMARY KEY,
                name VARCHAR(60) NOT NULL);""")
                print("Table \"game\" created successfully.")
                conn.commit()
                return True
    except OperationalError as oe:
        print("Un error ha ocurrido:", oe)

    finally:
        if conn is not None:
            conn.close()
