"""flattening the hetrogeneus list"""

lst = [35, 53, (525, 6743), 64, 63, [743, 754, 757]]

def flatten(lst):
    result = []
    if isinstance(lst, (list, tuple)):
        """ Isinstance returns True if the specified object is of the specified type, otherwise False 
           we had one nested list ans tuple in list so its True in our case 
           if we propose dictionary inside a list it will be false"""
        for x in lst:
            result.extend(flatten(x))
            """extending as well as appending the item to the empty list using function"""
    else:
        result.append(lst)
    return result
print(flatten(lst))





