#Write the missing function in the code below and decorate it properly, in order for the program to print out "I like solving coding exercises in Python. It's my hobby, really!".
### zadanie:
# def my_decorator(target):
#     def function_wrapper():
#         return "I like solving " + target() + " in Python. It's my hobby, really!"
#
#     return function_wrapper
#
#
# print(target())
###
def my_decorator(target):
    def function_wrapper():
        return "I like solving " + target() + " in Python. It's my hobby, really!"

    return function_wrapper


@my_decorator
def target():
    return "coding exercises"


print(target())

