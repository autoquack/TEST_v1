import random
#random pole o velkosti 10
array = []
array = [random.randint(0,20) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)


def test(array):
    return all(is_prime(i) for i in array)
def is_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True;
    else:
        for x in range(2 ,n):
            if (n % x == 0):
                return False
        return True
print("Original list of numbers:")
print(array)
print("Check if each number is prime in the said list of numbers:")
print(test(array))