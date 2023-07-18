zadanie_2 = """
- na vstupe z klavesnice nejaky text, ulohou spocitat kolko je (len)pismen (nie znakov&cisel)
- ak to pojde - spocitat kolko je samohlasok
"""
print(zadanie_2)

text_1 = input("Zadaj text:\n")
text_1 = text_1.lower()
pismena = 0
cisla = 0
znaky = 0
samohlasky = 0
samohlasky_def = "aáäeéiíyýoóuú"

for x in text_1:
    if x.isalpha():
        pismena += 1
    elif x.isdigit():
        cisla += 1
    else:
        znaky += 1

for y in text_1:
    if y in samohlasky_def:
        samohlasky = samohlasky+1

print("Pocet pismen =", pismena, "\nPocet cisel =", cisla, "\nPocet specialnych znakov =", znaky,"\nPocet samohlasok =", samohlasky)

#samohlasky = 0
#samohlasky = "a"

#text_1 = input("Zadaj text pre spocitanie pismen v texte:\n")
#count.text
#num_of_ch = len((text_1))
#num_of_ch = sum curses.ascii.isalpha(text_1)

#match
#count = text_1.count(samohlasky)
#matches = ["a", "e"]

#if any([y in text_1 for y in matches]):
#    print("samohlasky:", matches)

#for y in text_1:
#    if y == "a" "e":
#        samohlasky += 1
#    else:
#        pass

#print("Pocet samohlasok:", samohlasky)


#print("samohlasky sa vyskytuju: ", text_1.count("a","e"))
#samohlasky.count("a", "e")
#if "a" or "a" or "á" or "ä" or "e" or "é" or "i" or "í" or "y" or "ý" or "o" or "ó" or "u" or "ú" in text_1:
#    samohlasky = samohlasky +1
#if "A" or "E" in text_1:
#   samohlasky +=1




#print("Pocet samohlasok: ", text_1.count("a"))
#print("Pocet samohlasok: ", text_1.count("a", "á", "ä", "e", "é", "i", "í", "y", "ý", "o", "ó", "u", "ú"))

