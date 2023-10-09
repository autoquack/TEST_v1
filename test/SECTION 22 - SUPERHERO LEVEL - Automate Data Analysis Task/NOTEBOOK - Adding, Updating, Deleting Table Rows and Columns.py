Adding, Updating, Deleting
Table
Rows and Columns

# Adding Rows and Columns

# Adding a column to a DataFrame
djson["Badge ID"] = ["0010", "0011", "0012", "0013", "0014", "0015", "0016", "0017", "0018", "0019"]

# Adding a row / multiple rows to a DataFrame
djson = djson.append([{"Address": "11th Address, Miami",
                       "Department": "IT",
                       "FirstName": "John",
                       "ID": 11,
                       "LastName": "Doe",
                       "Phone": "09090977",
                       "Salary": "60000",
                       "Skills": "Java",
                       "Badge ID": "0020"},
                      {"Address": "12th Address, Miami",
                       "Department": "IT",
                       "FirstName": "Jake",
                       "ID": 12,
                       "LastName": "Winston",
                       "Phone": "09090988",
                       "Salary": "59000",
                       "Skills": "Python",
                       "Badge ID": "0021"},
                      {"Address": "13th Address, Miami",
                       "Department": "IT",
                       "FirstName": "Jacob",
                       "ID": 13,
                       "LastName": "Mueller",
                       "Phone": "09090999",
                       "Salary": "59600",
                       "Skills": "Routing",
                       "Badge ID": "0022"}], ignore_index=True)

# ...or using Series and append()
djson = djson.append(pandas.Series(
    ["14th Address, Miami", "Marketing", "Alice", 14, "Donovan", "88899901", "54000", "Instagram", "0023"],
    index=djson.columns), ignore_index=True)

# Updating Rows and Columns (modifying the DataFrame in place)

# Updating a column
djson["Badge ID"] = djson["FirstName"] + "2019"
djson["Badge ID"] = djson["Badge ID"] + "-2019"
djson["FirstName"] = djson.shape[0] * ["Jack"]

# Updating a column with string concatenation and list comprehensions
djson["Badge ID"] = [("00" + str(i)) for i in range(djson.shape[0])]

# Updating multiple rows based on a condition
djson.loc[djson["Department"] == "IT", "Salary"] = "90000"

# ...or, being more granular and using multiple conditions:
djson.loc[(djson["Department"] == "IT") & (djson["Skills"] == "Networking"), "Salary"] = "100000"

# Updating multiple fields on the same row
djson.loc[djson["ID"] == 9, ["Salary", "Phone"]] = ["80000", "555666777"]

# Deleting Rows and Columns

# Deleting a row by its name; by default, this command removes a row, if it is found
djson.drop("label")

# Deleting a row explicitly, by passing 0 or 'index' as an argument; drop labels from the index (0 or 'index')
djson.drop("label", 0)
djson.drop("label", "index")

# Deleting a row explicitly, by passing 0 or 'index' as an argument; drop labels from the index (0 or 'index'); modifying the DataFrame in place
djson.drop("label", 0, inplace=True)
djson.drop("label", "index", inplace=True)

# Deleting a column explicitly, by passing 1 or 'column' as an argument; drop labels from the columns (1 or 'columns')
djson.drop("label", 1)
djson.drop("label", "columns")

# Deleting a column explicitly, by passing 1 or 'column' as an argument; drop labels from the columns (1 or 'columns'); modifying the DataFrame in place
djson.drop("label", 1, inplace=True)
djson.drop("label", "columns", inplace=True)

# Deleting rows by indexes
djson.drop(djson.index[4])
djson.drop(djson.index[4], 0)

# Deleting rows by slices
djson.drop(djson.index[4:8])
djson.drop(djson.index[4:8], 0)

# Deleting columns by indexes
djson.drop(djson.columns[5], 1)

# Deleting columns by slices
djson.drop(djson.columns[3:5], 1)