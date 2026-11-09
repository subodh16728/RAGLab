import psycopg

from app.config import DATABASE_CONFIG

def get_db_connection():
    connection = psycopg.connect(**DATABASE_CONFIG)
    return connection