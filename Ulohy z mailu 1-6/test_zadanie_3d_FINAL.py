import random
#random pole o velkosti 10
array = []
array = [random.randint(0,1000) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

print("Tieto cisla su neparne: ")
#odd numer checking
for odd_number in array:
    if odd_number % 2 != 0:
#        print(odd_number)
#        print("Tieto cisla su neparne: ")
        print(odd_number, end=" ")

print("\nTieto cisla su parne: ")
for even_number in array:
    if even_number %2 == 0:
        print(even_number, end=" ")