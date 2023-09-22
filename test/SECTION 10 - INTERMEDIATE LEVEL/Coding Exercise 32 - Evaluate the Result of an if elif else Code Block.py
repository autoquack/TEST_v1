#Considering x = "Hello Python" and the following if/elif/else code block, analyze the code and write the result that it should return, in between the quotes of result.

'''
x = "Hello Python"

if x.startswith("H") or len(x) > 12:

	print('/'.join(x[:7]))

elif x[-1] == "n" and len(x.split('o')) >= 3:

    print(x.lower()[4:])

else:

	print((x + ' ') * 3 + "!")
'''

result = "H/e/l/l/o/ /P"

print(result)
