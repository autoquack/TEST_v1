import random
#random pole o velkosti 10
array = []
array = [random.randint(0,10) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

prime_array = []
notPrime_array = []

# If given number is greater than 1
for num in array:
    if num > 1:
    # Iterate from 2 to n / 2
      for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (num % i) == 0:
                notPrime_array.append(num)
                break
        else:
            prime_array.append(num)
    else:
        notPrime_array.append(num)
else:
        notPrime_array.append(num)


#for item in array:
#  if item is num:
#    prime_array.append(item)
print("not prime number", notPrime_array)
print("is prime number", prime_array)