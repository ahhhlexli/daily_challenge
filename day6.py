"""Create a function that given a string, 
it returns the middle character of the string. 
If the length of the string is even, return the two middle characters 
of the string."""

def middle(string):

    str_len = len(string)
    mid_index = str_len // 2

    if str_len % 2 == 0:
        middle_string = string[mid_index-1:mid_index+1]
    else:
        middle_string = string[mid_index]

    return middle_string

print(middle('123456'))

