import random
#random pole o velkosti 10
array = []
array = [random.randint(0,10) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

prime_array = []

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


for item in array:
  if item in is_prime(True):
    prime_array.append(item)
print(prime_array)