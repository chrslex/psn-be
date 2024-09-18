import mysql.connector
import os

def get_db_connection():
    conn = mysql.connector.connect(
        host = os.getenv('MYSQL_HOST', 'localhost'),
        user = os.getenv('MYSQL_USER', 'root'),
        password = os.getenv('MYSQL_PASSWORD', ''),
        database = os.getenv('MYSQL_DB', 'flaskdb')
    )
    return conn