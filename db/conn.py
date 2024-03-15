import psycopg as ps
from decouple import config
from psycopg import OperationalError, ProgrammingError
import logging


def connection():
    try:    
        conn = ps.connect(
            user = config('DB_USER'), 
            password=config('DB_PASSWORD'),
            host=config('DB_HOST', default='localhost'),
            )
        return conn
    except Exception as e:
        logging.info(f"Error connecting to the database: {e}")
        return None    

def close_conn(conn):
    try:
        if conn is not None and conn.open:
            conn.close()
    except (OperationalError,ProgrammingError) as er:
        print(f"Error closing the connection: {er}")