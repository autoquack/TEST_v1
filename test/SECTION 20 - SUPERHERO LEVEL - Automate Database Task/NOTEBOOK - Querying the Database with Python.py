cursor = connection.cursor()

cursor.execute("select * from mystaff.employees where salary > 50000;")
# cursor.execute("select * from mystaff.employees where last_name like '%Richard%';")
# cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
# cursor.execute("select * from mystaff.employees where department in ('Sales', 'IT');")

records = cursor.fetchall()

for record in records:
    print(record)