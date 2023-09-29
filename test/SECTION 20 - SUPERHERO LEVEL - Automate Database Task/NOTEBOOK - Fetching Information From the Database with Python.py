cursor = connection.cursor()

cursor.execute("select * from mystaff.employees where salary > 50000;")
# cursor.execute("select * from mystaff.employees where last_name like '%Emma%';")
# cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
# cursor.execute("select * from mystaff.employees where department in ('Sales', 'IT');")

# Fetching all the rows in a query result; returns a list
records = cursor.fetchall()

# Fetching the next 2 rows in a query result; returns a list
records = cursor.fetchmany(size=2)

# Fetching the next row in a query result; returns a tuple; returns None when no more records are available
# records = cursor.fetchone()

for record in records:
    print(record)