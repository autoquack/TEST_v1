import random
#random pole o velkosti 10
array = []
array = [random.randint(0,10) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

prime_numbers = array
for num in range(0, 1000):
    if is_prime(num):
        prime_numbers.append(num)

print(prime_numbers)


#def Prime(1, array):
 #   if 1 == array:
  #      return True
   # elif 1 % array == 0:
    #    return False

#    return Prime(1, array + 1)

#print(Prime, end=" ")

#def prime(array):
#    for i in range (1, array+1):
#        if (array/i).is_integer():
#            array.append(i)
#    if len(array)==2:
#        print("Prime")
#    else:
#        print("Not Prime")
#prime()