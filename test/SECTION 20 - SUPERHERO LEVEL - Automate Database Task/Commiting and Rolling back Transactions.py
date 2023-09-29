import psycopg2

try:
    connection = psycopg2.connect(database = "staff", user = "meny", password = "password", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

cursor = connection.cursor()

###

#cursor.execute("insert into mystaff3.employees (id,first_name,last_name,department,phone,address,salary) \
# values (7, 'Cyril', 'Sobota', 'Sales', '0193927302', '7th Street, Minas Ithil', 25000);")

#connection.commit()

#connection.close()

# Commiting (saving) the changes/transactions performed since the last commit()
#connection.commit()

# Rolling back (undoing) the changes/transactions performed since the last commit()
connection.rollback()

connection.close()