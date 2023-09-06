

list1 = ['foo', 'baz', 'bat', 'w']
list2 = ['foo word word word', 'word baz word word', 'word word word word', 'word word bat word']



print([any(x in element.split(' ') for x in list1) for element in list2])
print([any(x in element for x in list1) for element in list2])

###

import random
#random pole o velkosti 10
array = []
array = [random.randint(0,20) for i in range(10)]
#array_list = array
print("10 nahodne generovanych cisel:\n", array)

list1 = ['foo', 'baz', 'bat', 'w']
list2 = ['foo word word word', 'word baz word word', 'word word word word', 'word word bat word']