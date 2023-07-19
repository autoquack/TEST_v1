zadanie_3 = "vstup z klavesnice nejaky retazec znakov a nasledne vypisat stredne pismeno (v pripade ze je retazec parny, tak 2 pismena)"
print(zadanie_3)

text = input("Zadaj text:\n")

pocet_znakov = len(text)
#print (pocet_znakov)   #overenie celkoveho poctu znakov

x = pocet_znakov/2
#print(x)
y = int(x)

if float(x) == int (x):
    print("Stredne dva znaky pri parnom pocte znakov su:", (text[y-1:y+1]))
else:
    print("Stredny znak pri neparnom pocte znakov je:", (text[y]))

###########################################################################

#if ((pocet_znakov/2)%2) == 0:
#    print(text[x-1:x+1])
#else:
#    print(text[x])


##if pocet_znakov / 2 == float:
##    print(text[x])
##else:
##    print(text[x-1:x+1])

#x = float(pocet_znakov / 2)
#x = int
#print(x)   #zakladne rozdelenie textu
#
#if float(x%2) == 0:
#    print(text[x-1:x+1])
#else:
#    print(text[x-1])




#print(text[1:2])   #vypisanie znakov na pozicii
#for y in x:
#    if x.is_integer():



