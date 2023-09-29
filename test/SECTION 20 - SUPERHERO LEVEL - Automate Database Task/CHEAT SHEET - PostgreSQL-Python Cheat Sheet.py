import psycopg2

# Establishing the connection to the database and handling exceptions
try:
    connection = psycopg2.connect(database="staff", user="mihai", password="python", host="127.0.0.1", port="5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

# Creating a cursor
cursor = conn.cursor()

# Creating a table and defining the attributes for each column
cur.execute('''create table mystaff.employees
      (id int primary key not null,
       first_name varchar(25) not null,
       last_name varchar(25) not null,
       department varchar(25) not null,
       phone varchar(25)
       address varchar(50),
       salary int);''')

# Inserting data into a table
cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) \
 values (1, 'John', 'Smith', 'Sales', '0123456789', '1st Street, Miami', 50000), \
        (2, 'Jack', 'Doe', 'IT', '0213456742', '2nd Street, NY', 55000), \
        (3, 'Emily', 'Davids', 'Sales', '0123456999', '3rd Street, LA', 59000), \
        (4, 'Karen', 'Willson', 'Logistics', '0823556785', '4th Street, Las Vegas', 41000), \
        (5, 'Emma', 'Richard', 'Marketing', '0423453580', '5th Street, Denver', 40000);")

# Updating the department column for the row(s) where the value on the last_name column is Doe
cursor = connection.cursor()
cursor.execute("update mystaff.employees set department = 'Logistics' where last_name = 'Doe';")

# Deleting all the records in the database for which the value in the salary column is greater than 50000
cursor = connection.cursor()
cursor.execute("delete from mystaff.employees where salary > 50000;")

# Querying the database using the cursor
cursor = connection.cursor()

cursor.execute("select * from mystaff.employees where salary > 50000;")
# cursor.execute("select * from mystaff.employees where last_name like '%Richard%';")
# cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
# cursor.execute("select * from mystaff.employees where department in ('Sales', 'IT');")

# Fetching all the rows in a query result; returns a list
records = cursor.fetchall()

# Fetching the next 2 rows in a query result; returns a list
records = cursor.fetchmany(size=2)

# Fetching the next row in a query result; returns a tuple; returns None when no more records are available
records = cursor.fetchone()

# Printing the fetched results to the screen
for record in records:
    print(record)

# Commiting (saving) the changes/transactions performed since the last commit()
connection.commit()

# Rolling back (undoing) the changes/transactions performed since the last commit()
connection.rollback()

# Closing the connection to the database
connection.close()