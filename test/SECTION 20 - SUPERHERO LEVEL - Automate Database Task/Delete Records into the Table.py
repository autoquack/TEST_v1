
import psycopg2

try:
    connection = psycopg2.connect(database = "staff", user = "meny", password = "password", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

cursor = connection.cursor()

# Deleting all the records in the database for which the value in the salary column is greater than 50000

cursor = connection.cursor()
cursor.execute("delete from mystaff3.employees where salary > 50000;")
connection.commit()
connection.close()