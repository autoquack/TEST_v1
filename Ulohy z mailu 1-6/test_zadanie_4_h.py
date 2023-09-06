import random
#random pole o velkosti 10
array = []
array = [random.randint(0,1000) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

#intArray = [int(i) for i in array]
#print(intArray())

#for prime in array:
n = array[0]
for i in range(2,n):
    if n%i == 0:
        print(False)
        break
else:
    #else statement only happens if you don't break out of the loop
    print(True)

result = zip(array_list)
print(result)
