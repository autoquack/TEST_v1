import random
#random a pole
array = []
array = [random.randint(0,1000) for i in range(10)]

print(array)

#parne ci neparne

#range(1, len(array), 2)
#[i for i in range(len(array)) if i % 2 == 1]
#print()
#odd_numbers = array
# TOTO VYPISE LEN ARRAYE V NEJAKOM PORADI ATD
def odd_numbers(lst):
  odd_lst = []
  for index in range(1, len(lst), 2):
    odd_lst.append(lst[index])
  return odd_lst
print(odd_numbers(array))

def odd2_numbers(lst):
    odd2_lst = []
    [i for i in range(len(lst)) if i % 2 == 1]
 #       odd2.lst.appent(lst[index])
    return odd2_lst
print(odd2_numbers(array))
#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2, 6]))

# cez if else spravit