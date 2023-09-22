# Write the missing line of code so that the print() function at the end will print out Javascript as the final result.

#myfile = open("myfile.txt", "w")
#myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift")
#
#myfile = open("myfile.txt")
#
#This should return "Javascript\n"
#print(myfile.readlines()[2])
###########
myfile = open("myfile.txt", "w")

myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift")

myfile.close()

myfile = open("myfile.txt")

#This should return "Javascript\n"
print(myfile.readlines()[2])