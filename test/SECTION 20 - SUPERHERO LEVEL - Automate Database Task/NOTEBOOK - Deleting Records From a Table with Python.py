# Deleting all the records in the database for which the value in the salary column is greater than 50000

cursor = connection.cursor()
cursor.execute("delete from mystaff.employees where salary > 50000;")
connection.commit()
connection.close()a