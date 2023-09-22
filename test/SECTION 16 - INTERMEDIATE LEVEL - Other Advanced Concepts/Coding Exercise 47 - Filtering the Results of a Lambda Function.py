# Write code in between the parentheses of print(), that will extract the elements in range(10, 20) that are less than 16, in the form of a list, using filter() and a lambda function.
### zadanie:
#r1 = range(10, 20)

#print()
###
r1 = range(10, 20)

#print(r1(filter(lambda x, y: r1 < 16 )))
print(list(filter(lambda a: a < 16, r1)))
