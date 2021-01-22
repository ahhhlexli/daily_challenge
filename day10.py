"""
Given an integer, create a function that finds and returns the length 
of the longest binary gap of the binary representation of that integer. 
A binary gap is the sequence of consecutive zeros in between ones in a binary representation. 
Reference for binary representation can be found here: 
https://www.rapidtables.com/convert/number/decimal-to-binary.html"""

from itertools import groupby

def binary_zeros(number):

    number = list(bin(number).replace('0b', ''))
    groups = [list(g) for k, g in groupby(number)] 
    
    max_length = 0
    for group in groups:
        if '0' in group:
            length = len(group)
            if length > max_length:
                max_length = length

    return max_length 

print(binary_zeros(529))
print(binary_zeros(15))