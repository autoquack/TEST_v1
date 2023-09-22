#Considering x = "Hello Python" and the following if/elif/else code block, analyze the code and write the result that it should return, in between the quotes of result.
'''
x = "Hello Python"

if x.startswith("H") and len(x) > 12:

	print("'/'.join(x[:7])")

elif x[:-1] == "n" and len(x.split('o')) >= 3:

	for i in x.strip('n'):

	    print(i * 2)

else:

	print((x + ' ') * 3 + "!")
'''

result = "Hello Python Hello Python Hello Python !"

print(result)