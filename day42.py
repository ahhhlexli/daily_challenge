"""
Write a function that replaces each integer with the next largest in the list.

Examples

replace_next_largest([5, 7, 3, 2, 8]) ➞ [7, 8, 5, 3, -1]
replace_next_largest([2, 3, 4, 5]) ➞ [3, 4, 5, -1]
replace_next_largest([1, 0, -1, 8, -72]) ➞ [8, 1, 0, -1, -1]
"""
def replace_next_largest(l1):

    for i in range(len(l1)-1): 
        if l1[i+1] > l1[i]:
            temp = l1[i]
            l1[i] = l1[i+1]
            l1[i+1] = temp
        else:
            temp_max = max(l1[i:])
            temp_index = l1.index(temp_max)     
            l1[temp_index] = l1[i]
            l1[i] = temp_max
    l1[-1] = -1
    return l1

print(replace_next_largest([5, 7, 3, 2, 8]))
print(replace_next_largest([2, 3, 4, 5]))
print(replace_next_largest([1, 0, -1, 8, -72]))