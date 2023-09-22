import random
array = [random.randint(0,100) for i in range(10)]
print("10 nahodne generovanych cisel:\n", array)

isPrime_array = []
notPrime_array = []

def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):
        if num%n==0:
            return False
    return True

for number in array:
    if isprime(number) is True:
        isPrime_array.append(number)
    else:
        notPrime_array.append(number)

#print(isprime(13))
#print(isprime(18))

print("not prime number", notPrime_array)
print("is prime number", isPrime_array)
