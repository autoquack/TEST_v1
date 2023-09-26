#Write code in between the parentheses of list(), that will return a list consisting of all the odd integers in the r1 range that are greater than 6 and less than 16, using a function from within the itertools module.
###zadanie:
# from itertools import *
#
# r1 = range(1,21)
#
# my_list = list()
#
# print(my_list)
###
from itertools import *

r1 = range(1,21)

my_list = list(islice(r1, 6, 16, 2))

print(my_list)