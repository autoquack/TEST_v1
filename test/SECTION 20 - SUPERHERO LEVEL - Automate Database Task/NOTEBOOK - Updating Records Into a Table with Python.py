# Updating the department column for the row(s) where the value on the last_name column is Doe

cursor = connection.cursor()
cursor.execute("update mystaff.employees set department = 'Logistics' where last_name = 'Doe';")
connection.commit()
connection.close()