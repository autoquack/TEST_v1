import random
#random pole o velkosti 10
array = []
array = [random.randint(0,1000) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

#intArray = [int(i) for i in array]
#print(intArray())

#for prime in array:
#n = array[0]
#for i in range(2,n):
#    if n%i == 0:
#        print(False)
#        break
#else:
#    print(True)

def prime_number(n, d):
    if n//2 < d:
      return True
    if n%d == 0:
      return False
    return prime_number(n, d+1)

def find_primes(n,i, result):
  if i == n + 1:
    return result
  if prime_number(i, 2):
    result.append(i)
  return find_primes(n, i+1, result)

print(find_primes(100,2, []))
