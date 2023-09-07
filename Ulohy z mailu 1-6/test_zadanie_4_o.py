import random
#random pole o velkosti 10
array = []
array = [random.randint(0,10) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

prime_array = []
notPrime_array = []

#####
for num in array:
    if num == 1:
        notPrime_array.append(num)
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                notPrime_array.append(num)
            break
        else:
            prime_array.append(num)
    else:
        notPrime_array.append(num)



#for item in array:
#  if item is num:
#    prime_array.append(item)
print("not prime number", notPrime_array)
print("is prime number", prime_array)