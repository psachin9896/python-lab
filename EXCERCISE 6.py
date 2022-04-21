"""taken two list to verify """
list1 = [11, 222, 434, 564, 7869, 777, 558, 494, 411]
list2 = [11, 2543, 564, 325, 566, 777, 494, 9810]


# first asignment
def common_data(list1, list2):
    """ passing two list as parameter """
    result = False
    for i in list1:
        for j in list2:
            """checking if all the elements of list1 are present in in list2 or not """
            if i == j:
                result = True
    return result


"""passed list in square brackets to check the list rather than checking every elements"""
print(common_data([list1], [list2]))
print("*" * 20)

# second assingnment
"""writing files about the common data inside the two lists"""


def common_elements(list1, list2):
    """created a file object to print inside the file and used file= keyword to write """
    f = open("common_elements.txt", "w")
    for i in list1:
        if i in list2:
            print(i, file=f, end="\n")
    f.close()


common_elements(list1, list2)


# third assignment
def disjoint_elements(list1, list2):
    """created a file object to print inside the file and used file= keyword to write """
    f = open("disjoint_elements", "w")
    for i in list1:
        if i not in list2:
            print(i, file=f, end="\n")
    else:
        for i in list2:
            if i not in list1:
                print(i, file=f, end="\n")
    f.close()


disjoint_elements(list1, list2)
