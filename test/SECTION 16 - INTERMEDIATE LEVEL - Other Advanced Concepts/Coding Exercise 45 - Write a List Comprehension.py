#Write a list comprehension in between the parentheses of print() that will iterate over the [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] list and will multiply by 10 ONLY the elements that are greater than or equal to 7.
### zadanie:
#print()
###
print([x * 10 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x >= 7])