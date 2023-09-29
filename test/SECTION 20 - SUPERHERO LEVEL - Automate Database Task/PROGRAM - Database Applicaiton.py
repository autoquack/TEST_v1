import psycopg2

# Opening the text file for reading
f = open("C:\\Users\martin.haluska\Downloads\employees.txt")

# Creating an empty list for storing the records as a list of lists
records = []

# Splitting each line in the file by the "/ " delimiter and appending each list generated by readlines() to the new list, records
for i in f.readlines():
    records.append(i.split("/ "))

# print(records)

# Connecting to the database
try:
    connection = psycopg2.connect(database="staff", user="meny", password="password", host="127.0.0.1", port="5432")

except psycopg2.Error as err:
    print("An error was generated while connecting to the database!")

else:
    print("Connection to database was successful!\n")

# Initializing the cursor
cursor = connection.cursor()

# Iterating over the records list and, for each inner list, extracting the data associated with each of the 7 columns in the table using indexes and inserting the data in the table using the INSERT command
try:
    for i in records:
        cursor.execute(
            "insert into mystaff3.employees (id,first_name,last_name,department,phone,address,salary) values (%s,%s,%s,%s,%s,%s,%s);",
            (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

except psycopg2.Error as err:
    print("An error was generated while inserting the records!")

else:
    print("Records inserted successfully!\n")

# Committing (saving) the changes to the database
connection.commit()

for record in records:
    print(record)

# Closing the connection to the database
connection.close()

# End of Program