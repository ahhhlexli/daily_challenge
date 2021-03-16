"""Create a function that transposes a 2D matrix.

Examples

transpose_matrix([ [1, 1, 1], [2, 2, 2], [3, 3, 3] ]) ➞ [ [1, 2, 3], [1, 2, 3], [1, 2, 3] ]
transpose_matrix([ [5, 5], [6, 7], [9, 1] ]) ➞ [ [5, 6, 9], [5, 7, 1] ]
"""

def transpose_matrix(a):
    full_lst = [j for i in a for j in i]
    return [(lambda length: [full_lst[i] for i in range(length,len(full_lst),len(a[0]))])(length) for length in range(len(a[0])) ]

print(transpose_matrix([ [1, 1, 1], [2, 2, 2], [3, 3, 3] ]))
print(transpose_matrix([ [5, 5], [6, 7], [9, 1] ]))