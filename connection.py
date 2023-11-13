import mysql.connector

def db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="0987",
        database="food"
    )

    cursor = conn.cursor()
    return conn, cursor



