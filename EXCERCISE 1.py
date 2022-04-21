import itertools
"""flattening of list has done in three different ways"""
"""flattening of homogeneus list using list comprehension"""

List1 = [[1, 2, 3, 4], ['a', 'b', 'c'], [5, 'd']]
new_list = [item for item in List1 for item in item]
print(List1)
print(new_list)

print("_" * 100)


"""Flattening of list using two for loops """

new_list2 = []
for sublist in List1:
    for item  in sublist:
        new_list2.append(item)

print(List1)
print(new_list2)
print("_" * 100)

""" flattening the list using itertools method"""
List1 = [[1, 2, 3, 4], ['a', 'b', 'c'], [5, 'd']]

new_list3 = list(itertools.chain(*List1))

print(List1)
print(new_list3)
print("_" * 100)