from .conn import connection
from decouple import config
from psycopg import OperationalError, ProgrammingError

def check_db_exists():
    conn = connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""SELECT 1 FROM pg_database WHERE datname= %s """, (config('DB_NAME'),))
            exists = cur.fetchone()
            return True
    except (OperationalError, ProgrammingError) as e:
        print(f"ERROR CHECKING DB EXISTS Exeption",{e})
        return False
