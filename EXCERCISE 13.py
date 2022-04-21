# reversing the string using generator function

str = input("enter the string :")

def reverse_string(str):
    """ generator to reverse a string """
    length = len(str)
    """tried without length at first only with len() method and got error of 'str' and 'int' data types"""
    for i in range(length -1,-1,-1):
        yield str[i]

"""using for loop to reverse the string"""
for char in reverse_string(str):
    print(char)


