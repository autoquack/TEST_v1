import random
#random pole o velkosti 10
array = [random.randint(0,10) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

prime_array = []
notPrime_array = []


def is_prime(n):
  for i in range(2,int(n/2)):
    if (n%i) == 0:
      return False
  return True

for num in array:
    if is_prime is False:
        prime_array.append(num)
    else:
        notPrime_array.append(num)




print("not prime number", notPrime_array)
print("is prime number", prime_array)