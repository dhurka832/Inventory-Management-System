import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="**********",  
            database="inventory_db"
        )
        if connection.is_connected():
            return connection
    except Error as err:
        print("Error connecting to MySQL:", err)
    return None
