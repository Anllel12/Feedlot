import mysql.connector
from . import ConnectionAbs

class LocalConnection(ConnectionAbs):

    @staticmethod
    def connect():
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="feedlot"
            )
        except mysql.connector.Error as error:
            print(f"Error connecting to the database: {error}")