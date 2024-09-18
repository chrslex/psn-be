import mysql.connector

db = mysql.connector.connect(
    host="db",
    user="root",
    password="rootpassword",
    database="testdb"
)