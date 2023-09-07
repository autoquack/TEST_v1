import random
#random pole o velkosti 10
array = []
array = [random.randint(0,1000) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)



def isprime(array):
    if array > 1:
        for n in range(2, array):
            if (array % n) == 0:
                return False
        return True
        print(isprime, end=" ")
    else:
        return False
    print(isprime, end=" ")
