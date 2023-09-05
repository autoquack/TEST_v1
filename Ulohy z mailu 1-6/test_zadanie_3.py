uloha3 ="""
Uloha3:
- vytvoris pole o velkosti 10 prvkov, do ktoreho pomocou random funkcie vlozis cele cisla od 1 po 1000 a nasledne urcis ci dane cisla su parne alebo neparne
"""
print(uloha3)
import random
#field = ["prvok1", "prvok1", "prvok1", "prvok1", "prvok1", "prvok1", "prvok1", "prvok1"]

#print(field)

#field = ["pole"] *5
#print(field)

r_number = random.randint(1, 1000)

array_size = int(input("Zadaj pocet poli: "))

field = ["empty"] * array_size
field[0:array_size] = r_number

print(field)



##
for (int i=0; i < numbers.length; i++){

if (numbers[i] % 2 == 0)
System.out.println(numbers[i] + " is even number.");
else
System.out.println(numbers[i] + " is odd number.");

}
