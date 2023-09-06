import random
#random pole o velkosti 10
array = []
array = [random.randint(0,20) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)


for prime_number in array:
    if prime_number > 1:
        for i in range(2, prime_number):
            if (prime_number % i) == 0:
                print(prime_number, "nie je prvocislo")
                break
    else:
        print(prime_number, "je prvocislo")
###################
#if cislo > 1: # overenie podmienky
#    for i in range(2, cislo):
#         if (cislo % i) == 0:
#            print(cislo, "nie je prvocislo")
#            break
#    else:
#        print(cislo, "je prvocislo")