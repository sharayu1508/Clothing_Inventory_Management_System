import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sharayu15",
            database="clothing_inventory"
        )

        return connection

    except mysql.connector.Error as err:
        print("Database Connection Error:", err)
        return None