import random
#random pole o velkosti 10
array = []
array = [random.randint(0,10) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

#intArray = [eval(i) for i in array]

def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return (False, "nie je prvocislo")
        return (True, "Je prvocislo")
    return (False, "nie je prvocislo")

print(is_prime)
#print(is_prime(array))

#for alpha in array:
#    if alpha is False:
#        print(is_prime, end=" ")
#from array import *

for is_prime in array:
    if  is False:
    print(is_prime, end=" ")
