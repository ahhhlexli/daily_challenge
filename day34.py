"""In this challenge, you have to establish if a positive integer is a Modest number, accordingly to the following algorithm:

Divide the number into two left and right partitions. For each combination of left and right parts, 
you have to check if a condition is true: the remainder of the number divided by the right part is equal to the left part. 
If at least a combination of two parts satisfies the above condition, the number is Modest, otherwise, it's not. 
Given an integer num, implement a function that returns True if num is a Modest number, or False if it's not.

Example #1
is_modest(2036) ➞ True
Combination 1: Left = 2 | Right = 036 = 36 (Leading zeros are not considered) Number (2036) % Right (36) = 20 != Left (2)
Combination 2: Left = 20 | Right = 36 Number (2036) % Right (36) = 20 = Left (20)

At least a combination satisfies the condition
It's a Modest number
Example #2
is_modest(3412) ➞ False
Combination 1: Left = 3 | Right = 412 3412 % 412 = 116 != Left
Combination 2: Left = 34 | Right = 12 3412 % 12 = 4 != Left
Combination 3: Left = 341 | Right = 2 3412 % 2 = 0 != Left

It's not a Modest number
Notice how left and right parts are made:
They are not permutations or combinations...
...but partitions of consecutive digits.
Example #3
is_modest(21333) ➞ True
Combination 1: Left = 2 | Right = 1333 21333 % 1333 = 5 != Left
Combination 2: Left = 21 | Right = 333 21333 % 333 = 21 = Left

At least a combination satisfies the condition
It's a Modest number
Example #4
is_modest(8) ➞ False

An integer with less than two digits can't be partitioned.
"""

def is_modest(num):
    print(f'{num} is:')
    num_list = [i for i in str(num)]
    for i in range(len(num_list)-1):
        left = int(''.join(num_list[:i+1]))
        right = int(''.join(num_list[i+1:]))
        if (num % right == left):
            return True 
    
    return False

print(is_modest(8))
print(is_modest(2036))
print(is_modest(3412))
print(is_modest(21333))