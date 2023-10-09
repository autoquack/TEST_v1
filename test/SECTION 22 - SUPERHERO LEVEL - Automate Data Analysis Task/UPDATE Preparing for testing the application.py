Before testing the application, make sure that you:

Download all the files from the next lecture - the PandasApp.py script and the 4 my_employees files, and save them inside a directory on your hard-drive.

Open PSQL and check the existing database, schema and table (the ones from the Database Automation section):

postgres=# \c staff;
staff=# select * from mystaff.employees;
 id | first_name | last_name | department |   phone    |        address        | salary
----+------------+-----------+------------+------------+-----------------------+--------
  1 | John       | Smith     | Sales      | 0123456789 | 1st Street, Miami     |  50000
  2 | Jack       | Doe       | IT         | 0213456742 | 2nd Street, NY        |  55000
  3 | Emily      | Davids    | Sales      | 0123456999 | 3rd Street, LA        |  59000
  4 | Karen      | Willson   | Logistics  | 0823556785 | 4th Street, Las Vegas |  41000
  5 | Emma       | Richard   | Marketing  | 0423453580 | 5th Street, Denver    |  40000
  6 | Jane       | Sanders   | HR         | 1811919191 | 6th Street, Miami     |  61000
(6 rows)
If your database table doesn't look like the one above, then you can obtain it by deleting all the existing entries in your table and inserting them once again, using the commands below:

staff=# delete from mystaff.employees;
DELETE 5
insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) \
 values (1, 'John', 'Smith', 'Sales', '0123456789', '1st Street, Miami', 50000), \
        (2, 'Jack', 'Doe', 'IT', '0213456742', '2nd Street, NY', 55000), \
        (3, 'Emily', 'Davids', 'Sales', '0123456999', '3rd Street, LA', 59000), \
        (4, 'Karen', 'Willson', 'Logistics', '0823556785', '4th Street, Las Vegas', 41000), \
        (5, 'Emma', 'Richard', 'Marketing', '0423453580', '5th Street, Denver', 40000), \
        (6, 'Jane', 'Sanders', 'HR', '1811919191', '6th Street, Miami', 61000);