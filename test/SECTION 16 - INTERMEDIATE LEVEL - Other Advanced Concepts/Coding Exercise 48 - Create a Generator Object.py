#Considering the code below, the this_func() function returns the result of x * i / y, when called, resulting in an floating-point number.

#def this_func(x, y):
#    for i in range(5):
#        return x * i / y

#This function will return a float:

#a = this_func(10, 5)
#type(a)
#<class 'float'>

#How would you change this function in order to have a generator object returned when calling the function, not an integer?
### zadanie:
# def this_func(x, y):
#     for i in range(5):
#
#
# a = this_func(5, 10)
#
# print(type(a))  # this should return <class 'generator'> in the end
# ###
def this_func(x, y):
    for i in range(5):
        yield x * i / y

a = this_func(5, 10)

print(type(a))  # this should return <class 'generator'> in the end



