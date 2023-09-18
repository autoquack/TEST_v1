#zadanie = "Select option which you want to execute:\nPress 1 to encrypt text\nPress 2 to decrypt text"
#print(zadanie)
#menu = int(input("Select option which you want to execute:\nPress 1 to encrypt text\nPress 2 to decrypt text\n"))
#print(menu)
############################################################
#menu na zvolenie sifrovania/desifrovania
def menu():
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
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
def key():
    print("Choose encryption/decryption key value from 1-25:\n")
    global keyOptions
    keyOptions = int(input())
    if 0 < keyOptions < 26:
        print("you chose key", keyOptions)
#    elif keyOptions > 26: (0 >= key <= 26):
#        print("you choose key 2")
    else:
        return key()
key()
print(keyOptions)
#Alpha = key(keyOptions)
#key2 = key()
#print(key())

###########################################################
def cipher(text, cipherKey):
    result = ""


    for i in range(len(text)):
        char = text[i]


        if (char.isupper()):
            result += chr((ord(char) + cipherKey - 65) % 26 + 65)


        else:
            result += chr((ord(char) + cipherKey - 97) % 26 + 97)

    return result


text = input("Insert text to decipher:\n")
#text = "jelenovipivonelej"
cipherKey = keyOptions
print("Cipher: " + cipher(text, cipherKey))

