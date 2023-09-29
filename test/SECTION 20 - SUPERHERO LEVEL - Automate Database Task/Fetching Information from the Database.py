import psycopg2

try:
    connection = psycopg2.connect(database = "staff", user = "meny", password = "password", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

cursor = connection.cursor()

###

cursor.execute("select * from mystaff3.employees where salary > 40000;")
# cursor.execute("select * from mystaff.employees where last_name like '%Emma%';")
# cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
# cursor.execute("select * from mystaff.employees where department in ('Sales', 'IT');")

# Fetching all the rows in a query result; returns a list
#records = cursor.fetchall()

# Fetching the next 2 rows in a query result; returns a list
records = cursor.fetchmany(size=2)

# Fetching the next row in a query result; returns a tuple; returns None when no more records are available
# records = cursor.fetchone()

for record in records:
    print(record)