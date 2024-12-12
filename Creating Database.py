import mysql.connector
from mysql.connector import Error

def create_database():
    # Prompt the user for the database name
    db_name = input("Enter the name of the database: ")

    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(host='localhost',user='root',password='moksh24')
        if connection.is_connected():
            cursor = connection.cursor()
            # Check if the database already exists
            cursor.execute("SHOW DATABASES")
            databases = [row[0] for row in cursor.fetchall()]
            if db_name in databases:
                print(f"Database '{db_name}' already exists.")
            else:
                # Create the database using the execute command
                cursor.execute(f"CREATE DATABASE {db_name}")
                print(f"Database '{db_name}' created successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()

