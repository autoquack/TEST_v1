import random
#random pole o velkosti 10
array = []
array = [random.randint(0,10) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

prime_array = []


# If given number is greater than 1
for num in array:
    if num > 1:
    # Iterate from 2 to n / 2
      for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
    else:
            print(num, "is a prime number")
else:
        print(num, "is not a prime number")


#for item in array:
#  if item is num:
#    prime_array.append(item)
#print(prime_array)