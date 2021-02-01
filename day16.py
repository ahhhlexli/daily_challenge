""" 
Given an integer n, find all the integers that is the multiple of 3 from 0 to n. 
Return the sum of all these integers.

Input: 
10

Multiples of 3 from 0 to 10:
3, 6, 9

Return sum of these integers:
18
"""

def multiple_sum(number):

    multiples = [i for i in range(number) if i % 3 == 0]

    return sum(multiples)

print(multiple_sum(10))


