
###

import random
#random pole o velkosti 10
array = []
array = [random.randint(0,20) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

#intArray = [eval(i) for i in array]

# using list comprehension to
# perform conversion
intArray = [int(i) for i in array]
#array = int()
#array = int(input()).
print(intArray)

#n = int(input("Enter a number: "))
for i in array:
    if (i % array) == 0:
        print(False)
        break
else:
    #else statement only happens if you don't break out of the loop
    print(True)

#for primeNumber in array:
#    if (primeNumber % 1) == 0:
#        print(primeNumber, "is not prime", end=" ")
#        break
#    else:
#        print(primeNumber, "is prime", end=" ")

#for primeNumber in intArray:
#    if primeNumber > 1:
#        for primeNumber in range (2, primeNumber):
#            if (primeNumber % 1) == 0:
#                print(primeNumber, "nie je prvocislo", end=" ")
#                break
#        else:
#            print (primeNumber, "je prvocislo", end=" ")


#if array > 1: # overenie podmienky
#    for primeNumber in range(2, array):
#         if (array % primeNumber) == 0:
#            print(array, "nie je prvocislo")
#            break
#    else:
#        print(intArray, "je prvocislo")