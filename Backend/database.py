import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="RIDDHI@134",
            database="clothing_inventory"
        )
        if connection.is_connected():
            print("Database Connected Successfully!")
        return connection

    except mysql.connector.Error as err:
        print("Database Connection Error:", err)
        return None
    
if __name__=="__main__":
    conn = get_connection()

    if conn:
        print("Database connected Successfully!")
    else:
        print("Database connection Failed!")