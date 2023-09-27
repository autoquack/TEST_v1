import math

while True:
    print("Choose math operation:\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to power\n"
          "6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent")

    oper = input("\nYour option from the menu: ")
########## 0 - Addition ##########
    if oper == "0":
        value1 = float(input("\n---Addition---\nAdd value:\n"))
        value2 = float(input("\nTo value:\n"))
        print("\nThe result is: "+str(value1 + value2) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break

########## 1 - Subtraction ##########
    if oper == "1":
        value1 = float(input("\n---Subtraction---\nSubtract from value:\n"))
        value2 = float(input("\nValue:\n"))
        print("\nThe result is: "+str(value1 - value2) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break
########## 2 - Multiplication ##########
    if oper == "2":
        value1 = float(input("\n---Multiplication---\nMultiply value:\n"))
        value2 = float(input("\nBy value: \n"))
        print("\nThe result is: "+str(value1 * value2) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break
########## 3 - Division ##########
    if oper == "3":
        value1 = float(input("\n---Division---\nDivide value: \n"))
        value2 = float(input("\nBy value: \n"))
        print("\nThe result is: "+str(value1 / value2) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break
########## 4 - Modulo ##########
    if oper == "4":
        value1 = float(input("\n---Modulo---\nFirst value: \n"))
        value2 = float(input("\nSecond value: \n"))
        print("\nThe result is: "+str(value1 % value2) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break
########## 5 - Raising to power ##########
    if oper == "5":
        value1 = float(input("\n---Raising to power---\nInsert value of number: \n"))
        value2 = float(input("\nRaise to power by value: \n"))
        print("\nThe result is: "+str(value1 ** value2) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break
########## 6 - Square root ##########
    if oper == "6":
        value1 = float(input("\n---Square root---\nInsert value to calculate square root: \n"))
        print("\nThe result is: "+str(math.sqrt(value1)) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break
########## 7 - Logarithm ##########
    if oper == "7":
        value1 = float(input("\n---Logarithm---\nInsert value to calculate logarithm to base 2:\n"))
        print("\nThe result is: "+str(math.log(value1, 2)) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break
########## 8 - Sine ##########
    if oper == "8":
        value1 = float(input("\n---Sine---\nInsert value (in degrees) to calculate sinus:\n"))
        print("\nThe result is: "+str(math.sin(math.radians(value1))) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break
########## 9 - Cosine ##########
    if oper == "9":
        value1 = float(input("\n---Cosine---\nInsert value (in degrees) to calculate cosine:\n"))
        print("\nThe result is: "+str(math.cos(math.radians(value1))) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break
########## 10 - Tangent ##########
    if oper == "10":
        value1 = float(input("\n---Tangent---\nInsert value (in degrees) to calculate tangent:\n"))
        print("\nThe result is: "+str(math.tan(math.radians(value1))) + "\n")

        back = input("\nGo back to the main menu? (Y/N)\n")
        backLower = back.lower()
        if backLower == "y":
            continue
        else:
            break