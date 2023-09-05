uloha6="""
Uloha6:
Praca so subormi (opat na to existuju kniznice)
 - sucastou tejto ulohy bude vytvorit jednoduchy textovy subor (*.txt) a nasledne do neho zapisat vstup z klavesnice
 - nacitat existujuci subor a vypisat jeho obsah do konzoly
 - prepisat cely obsah existujuceho suboru
 - do existujuceho suboru kod napise datum a cas a nasledne ty pod tento udaj vlozis nove data (ako vstup z klavecnice)
    -> toto spravis 2 sposobmi 1: novy zaznam v subore bude uplne navrchu
                                                2: novy zaznam v subore bude na spodku
      Ako by to mohlo vyzerat (priklad)
  7/21/2023 14:55
   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

 7/21/2023 15:00
   Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.
 - nastuduj si kniznicu pre pracu s csv, xlsx subormi
"""
print(uloha6)

#create name of new txt file + default content of file
name1 = input("Zadaj nazov suboru ktory sa vytvori: \n")
original_content = input("Zadaj obsah suboru: \n")
nameFinal1 = name1 + '.txt'
print("Subor", nameFinal1, "bol vytvoreny.")
file1 = open("C:\\Users\martin.haluska\Downloads\pythonTestFolder/"+nameFinal1, "w")
file1.write(original_content)
file1.close()
#

#open file in folder
name2 = input("Zadaj ktory subor sa ma otvorit: \n")
file2 = open("C:\\Users\martin.haluska\Downloads\pythonTestFolder//"+name2, "r+")
print(file2.read())
file2_rewrite: str = input("Zadaj novy obsah suboru "+name2+":\n")
file2.write(file2_rewrite)
file2.close()
#write text

#file.read(file)
#file_rewrite = input("Zadaj text ktorym sa prepise obsah suboru:\n")
#file.write(file_rewrite)









import os

#file_name = input("Zadaj nazov suboru: \n")
#file = open("C:\Users\martin.haluska\Downloads\pythonTestFolder", file_name, "w")   # 'r' for reading and 'w' for writing
#file.write("Hello World from " + f.name)    # Write inside file
#file.close()

#file = open("C:\\Users\martin.haluska\Downloads\pythonTestFolder/test.txt", "w")   # 'r' for reading and 'w' for writing
#file.write("Hello World from " + f.name)    # Write inside file
#file.close()




#    try:
#        file = open(name,'r+')   # Trying to create a new file or open one
#        return file

#    except:
#        print('Something went wrong! Can\'t tell what?')
#        sys.exit(0) # quit Python

#a = write(numbers[num1] )