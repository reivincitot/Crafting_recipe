from .conn import connection
from decouple import config
from psycopg import OperationalError, ProgrammingError


def check_db_exists():
    conn = connection(db_name="postgres")
    dbname = config("DB_NAME")
    try:
        with conn.cursor() as cur:
            cur.execute("""SELECT 1 FROM pg_database WHERE datname= %s """, (dbname,))
            exists = cur.fetchone()
            return exists is not None
    except (OperationalError, ProgrammingError) as e:
        print(f"ERROR CHECKING DB EXISTS Exeption", {e})
        return False
