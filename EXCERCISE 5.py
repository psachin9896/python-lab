"""making dictionsry none free using dictionary comprehension"""

dict1 = {'a': 1, 'b': 2, 'c': None, 'd': 'z', 'e': None}

new_dict = {key: value for key, value in dict1.items() if value is not None}
""" dict.items method is used to iterate through dictionary and one if condition """
print(new_dict)


