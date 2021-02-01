""" 
Given two lists of any data type, return a list that combines the two lists 
by alternating the elements passed. The input lists can be of different lengths.
"""

def list_zipper(list1, list2):

    zipped = list(zip(list1, list2))
    final = []
    for i in zipped:
        for j in i:
            final.append(j)
    return final


list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

print(list_zipper(list1, list2))