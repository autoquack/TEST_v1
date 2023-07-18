def multiplynumbers(number1, number2):
    print (number1 * number2)

multiplynumbers(5,6)
multiplynumbers(2,4)

for number in range(999):
    multiplynumbers(number,number)

def add_number(alpha,beta):
    return alpha + beta

add_number(7,8)


print (add_number)


def print_list(list):
    for item in list:
        print(item)

print_list([1,2,4,8,16,32,64,128,256,512,1024])