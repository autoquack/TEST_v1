#zadanie = "Select option which you want to execute:\nPress 1 to encrypt text\nPress 2 to decrypt text"
#print(zadanie)
#menu = int(input("Select option which you want to execute:\nPress 1 to encrypt text\nPress 2 to decrypt text\n"))
#print(menu)
############################################################
#menu na zvolenie sifrovania/desifrovania
def menu():
    global menuOptions
    menuOptions = input("Select option which you want to execute:\nPress 1 to encrypt text\nPress 2 to decrypt text\n")
#    options = int(input("Select option which you want to execute:\nPress 1 to encrypt text\nPress 2 to decrypt text\n")) #s int() to nejde
    if menuOptions == "1":
        print("You chose encryption")
    elif menuOptions == "2":
        print("You chose decryption")
    else:
        return menu() #navrat na zaciatok ak zle hodnoty
menu() #spustenie def menu


############################################################
#definovanie posunu
def key():
    if menuOptions == 1:
        print("Choose encryption key value from 1-25:\n")
    else:
        print("Choose decryption key value from 1-25:\n")
    global keyOptions
    keyOptions = int(input())
    if 0 < keyOptions < 26:
        print("You chose key", keyOptions)
#    elif keyOptions > 26: (0 >= key <= 26):
#        print("you choose key 2")
    else:
        return key()
key()
#print(keyOptions)
#Alpha = key(keyOptions)
#key2 = key()
#print(key())

###########################################################
#kryptovanie a dekryptovanie
def cipher(text, cipherKey):
    result = ""
    if menuOptions == 1:
        for i in range(len(text)):
            char = text[i]


            if (char.isupper()):
                result += chr((ord(char) + cipherKey - 65) % 26 + 65)

            else:
                result += chr((ord(char) + cipherKey - 97) % 26 + 97)

        return result
    else:
        for i in (text)):
#            char = text[i]
            if i in text:
                position = text.find(i)
                new_pos = (position - cipherKey) % 26
                new_char = text[new_pos]
                result += new_char
            else:
                result += i
#            if (char.isupper()):
#                char.find(ch)
#                result += chr((ord(char) - cipherKey - 65) % 26 + 65)
#            else:
#                result += chr((ord(char) - cipherKey - 97) % 26 + 97)
        return result
''
#vlozenie textu
if menuOptions == 1:
    text = input("Insert text to encrypt:\n")
else:
    text = input("Insert text to decrypt:\n")
#text = "skuska"

# vysledok plus zvysok
cipherKey = keyOptions
if menuOptions == 1:
    print("Encrypted text: " + cipher(text, cipherKey))
else:
    print("Decrypted text: " + cipher(text, cipherKey))

