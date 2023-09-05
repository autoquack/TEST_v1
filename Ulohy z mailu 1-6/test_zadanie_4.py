uloha4="""
Uloha4:
- vytvoris pole o velkosti 10 prvkov, do ktoreho pomocou random funkcie vlozis cele cisla od 1 po 1000 a nasledne urcis ci dane su prvocisla alebo nie su prvocisla
"""
print(uloha4)

# vypocet prvocisla
cislo = int(input("Zadaj cislo:\n"))

if cislo > 1: # overenie podmienky
    for i in range(2, cislo):
         if (cislo % i) == 0:
            print(cislo, "nie je prvocislo")
            break
    else:
        print(cislo, "je prvocislo")
    # Else if the input number is less than or equal to 1
#else:
#    print(cislo, "nie je prvocislo")


#random cislo tvorba
import random
r_number = random.randint(1, 1000)

array_size = int(input("Zadaj pocet poli: "))

field = ["empty"] * array_size
field[0:array_size] = r_number

print(field)

#tvorba pola
import random
fields = ["prvok1", "prvok1", "prvok1", "prvok1", "prvok1", "prvok1", "prvok1", "prvok1"]

#print(field)

#field = ["pole"] *5
#print(field)

r_number = random.randint(1, 1000)

array_size = int(input("Zadaj pocet poli: "))

fields = ["empty"] * array_size
fields[0:array_size] = r_number

print(fields)

#porovnanie arrayu
for field in fields:
    if field ==