import psycopg2
from psycopg2 import OperationalError

def connect():

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="1234"
        )
        print("✓ Connected to database")
        return conn
    except OperationalError as e:
        return None
    
