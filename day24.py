"""
Given a number, return the difference between 
the maximum and minimum numbers that can be formed 
when the digits are rearranged.
"""

from itertools import permutations

def rearranged_diff(n):
    
    perms = list(permutations([i for i in str(n)]))
    max_perm = int(''.join(max(perms)))
    min_perm = int(''.join(min(perms)))
    
    print(f'Max: {max_perm} Min: {min_perm}')

    return max_perm - min_perm

print(rearranged_diff(1456))