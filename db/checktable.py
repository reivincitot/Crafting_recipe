from .conn import connection
from psycopg import Error


def check_tables(table_name, db_name):
    conn = connection(db_name)
    if conn is None:
        return False

    try:
        with conn.cursor() as curr:
            # Ejecuta una consulta SQL para verificar la existencia de la tabla
            curr.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
            exists = curr.fetchone()[0]
            return exists
    except Error as e:
        print("Error al ejecutar la consulta SQL", e)
        return False
    finally:
        if conn is not None:
            conn.close()
