import mysql.connector
import os
import time

def get_db_connection(retries=5, delay=3):
    for i in range(retries):
        try:
            conn = mysql.connector.connect(
                host = os.getenv('MYSQL_HOST', 'localhost'),
                user = os.getenv('MYSQL_USER', 'root'),
                password = os.getenv('MYSQL_PASSWORD', ''),
                database = os.getenv('MYSQL_DB', 'flaskdb')
            )
        except:
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
        return conn
    raise ConnectionError("Failed to connect to the database after several attempts.")