"""Given a list of integers, split the list into two, put the arrays on top of each other, 
then add them together. Return the finished list.
Example:

Input:
[1, 2, 3, 4, 5, 6, 7]

Putting on top:

[1, 2, 3]
[4, 5, 6, 7]

Adding up process:

[1, 2, 3]
+
[4, 5, 6, 7]

------------
[5, 7, 9, 7]
Returns:
[5, 7, 9, 7]
"""

def list_adder(input_list):

    halfpoint = len(input_list) // 2
    
    first_half = input_list[:halfpoint]
    second_half = input_list[halfpoint:]

    for i in range(len(first_half)):
        second_half[i] += first_half[i]
    
    return second_half

print(list_adder([1, 2, 3, 4, 5, 6, 7]))