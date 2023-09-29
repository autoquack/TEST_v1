
import psycopg2

try:
    connection = psycopg2.connect(database = "staff", user = "meny", password = "password", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

cursor = connection.cursor()



# Updating the department column for the row(s) where the value on the last_name column is Doe

cursor = connection.cursor()
cursor.execute("update mystaff3.employees set department = 'Logistics' where last_name = 'Doe';")
connection.commit()
connection.close()