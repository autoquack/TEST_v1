# Considering the following code, you have to perform two tasks in order to avoid any errors and get the correct result.
#
# Add the appropriate file access mode when opening the file for the second time, on line 7. The role of this line is to open the file again so we can add new data at the end of the file, without overwriting the existing data and to also allow us to read the file, at the same time.
#
# Add the appropriate method in between the parentheses of print(), in order to print out the newly added row in the file, Ruby. This method generates a list where each row in the file is an element of that list. Then, using the correct index, you can extract Ruby from the list.

#myfile = open("myfile2.txt", "w")

#myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift\n")

#myfile.close()

#myfile = open("myfile2.txt", )

#myfile.write("Ruby")

#myfile.seek(0)

#This should return "Ruby"
#print()
####
myfile = open("myfile2.txt", "w")

myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift\n")

myfile.close()

myfile = open("myfile2.txt", "a+")

myfile.write("Ruby")

myfile.seek(0)

#This should return "Ruby"
print(myfile.readlines()[-1])
