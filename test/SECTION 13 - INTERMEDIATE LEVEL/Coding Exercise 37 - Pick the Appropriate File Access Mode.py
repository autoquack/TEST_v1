#Add the correct file access mode to avoid getting the io.UnsupportedOperation error returned when running the code.

#myfile = open("myfile2.txt", )

#myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift")

#myfile.seek(0)

#This should return "Javascript"
#print(myfile.readlines()[2])

myfile = open("myfile2.txt", "w+")

myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift")

myfile.seek(0)

# This should return "Javascript"
print(myfile.readlines()[2])