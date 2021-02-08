""" 
Given a list of mixed integers of different representations, add up the non-string integers and subtract this from the total of string integers.

Example:

Input:
[1, '2', 3, '4', 5]

Output:
-3, because:
total of non-string integers = 1+3+5 = 9
total of string integers = 2+4 = 6
total of string integers - total of non-string integers = -3 
"""

def string_dif(num_list):
    str_sum = 0
    num_sum = 0
    for i in num_list:
        if type(i) == str:
            str_sum += int(i)
        elif type(i) == int:
            num_sum += i
    return str_sum - num_sum

print(string_dif([1, '2', 3, '4', 5]))