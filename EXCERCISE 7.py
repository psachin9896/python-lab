# printing the union of two dict.
d1={'a':1, 'b':2, 'c':3}
d2={'a':4, 'd':'e'}

"""created a function to print union of two dictionaries"""
def union(d1,d2):
    """using list concatenation inside dict. if we remove dict in return we will get the output as list
    and again we have to add dict in print keyword"""

    """doing of d1.items + d2.items rather than converting into list throws
     an error of unsupportive operand"""
    return dict(list(d1.items()) + list(d2.items()))

print(union(d1,d2))
print("_" * 80)

""" here is a another wat to create the union between two dictionaries"""

for key, value in d2.items():
    d1[key] = value

print(d1)
print("_" * 80)
""" here i have iterated on both of the dictionaries and i assure that if dict found any duplicate value
it always takes the larger value associated with common key"""

for key, value in d1.items():
    d2[key] = value

print(d2)
print("_" * 80)

