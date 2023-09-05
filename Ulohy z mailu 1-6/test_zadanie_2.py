uloha2 = """
Uloha2: DONE
- vstup z klavecnice bude cele cislo a pre dane cislo vypocitas faktorial
- vytvoris pole o velkosti 10 prvkov, do ktoreho pomocou random funkcie vlozis cele cisla od 1 po 1000 a nasledne urcis ci dane cisla su parne alebo neparne
"""
print(uloha2)

cislo = int(input("Zadaj cislo:"))
print(cislo)
fact = 1

for x in range(1, cislo + 1):
    fact = fact * x

print("The factorial of", cislo, "is", fact)


#fact = cislo*(cislo-1)

#factx = cislo*(cislo+1)
#print(fact)
#print(factx)

