Introduction
to
Pandas - Basic
Operations

# Installing Pandas in the Windows command line

pip
install
pandas

# Importing the Pandas module

import pandas

# Creating a data frame (the object holding the data) and passing a list of lists as an argument

d = pandas.DataFrame(
    [['Andy', 46, 'Engineer'], ['Jane', 33, 'Nurse'], ['Robert', 21, 'Student'], ['Maria', 30, 'Student']])

# The result, where 0, 1, 2 are the columns and 0, 1, 2, 3 are the indexes

d

0
1
2
0
Andy
46
Engineer
1
Jane
33
Nurse
2
Robert
21
Student
3
Maria
30
Student

# Checking that a DataFrame was indeed created

type(d)
pandas.core.frame.DataFrame

# Checking all the available methods and attributes for the DataFrame object

dir(d)

# Setting names for the columns - the number of elements of the columns list must match the number of elements in each of the lists containing the data

d = pandas.DataFrame(
    [['Andy', 46, 'Engineer'], ['Jane', 33, 'Nurse'], ['Robert', 21, 'Student'], ['Maria', 30, 'Student']],
    columns=['Name', 'Age', 'Occupation'])

# Setting names for the indexes - the number of elements of the index list must match the number of records in the table

d = pandas.DataFrame(
    [['Andy', 46, 'Engineer'], ['Jane', 33, 'Nurse'], ['Robert', 21, 'Student'], ['Maria', 30, 'Student']],
    columns=['Name', 'Age', 'Occupation'], index=['ID1', 'ID2', 'ID3', 'ID4'])

# Series objects

d.Name
d.Age
d.Occupation

type(d.Age)
pandas.core.series.Series

# Examples of specific methods

d.min()
d.Age.min()
d.Name.max()

More
information:

https: // pandas.pydata.org / pandas - docs / stable /