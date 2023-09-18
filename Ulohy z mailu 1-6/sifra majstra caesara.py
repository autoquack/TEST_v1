#zadanie = "Select option which you want to execute:\nPress 1 to encrypt text\nPress 2 to decrypt text"
#print(zadanie)

#option = int(input())

#print(option)


#def uvod():
#    print("Select option which you want to execute:\nPress 1 to encrypt text\nPress 2 to decrypt text")
#    option2 = int(input())
#    print(option2)

#print(uvod())

#for response in uvod():
#    if uvod == 1 :
#        print("enkryptacia nasledujuceho textu:")
#        break;
#    else:
#        uvod()


while True:
    uvod = input("Select option which you want to execute:\nPress 1 to encrypt text\nPress 2 to decrypt text\n")
    if uvod.lower() not in ("1"):
        print(uvod(), "bla bla bla")
        break
    else:
        #we're happy with the value given.
        #we're ready to ex3it the loop.
        continue

#while True:
#    data = input("Pick an answer from A to D:")
#    if data.lower() not in ('a', 'b', 'c', 'd'):
#        print("Not an appropriate choice.")
#    else:
#        break



