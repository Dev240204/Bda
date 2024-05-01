import mysql.connector

# MySQL connection parameters
mysql_host = 'mysql'  # MySQL service name in the Docker network
mysql_port = '3306'
mysql_user = 'root'
mysql_password = 'example'
mysql_database = 'hello'

# Connect to the MySQL database
connection = mysql.connector.connect(
    host=mysql_host,
    port=mysql_port,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

if connection.is_connected():
    print("Connected to MySQL database")
    # Proceed with executing queries
    cursor = connection.cursor()

    # Example: Fetch data from a table named 'your_table'
    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()

    # Print fetched data
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
else:
    print("Failed to connect to MySQL database")