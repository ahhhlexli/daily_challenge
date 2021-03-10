"""
Write a function that returns the closest palindrome number to an integer. If two palindrome numbers tie in absolute distance, return the smaller number.

Examples

closest_palindrome(887) ➞ 888

closest_palindrome(100) ➞ 99

99 and 101 are equally distant, so we return the smaller palindrome.
closest_palindrome(888) ➞ 888

closest_palindrome(27) ➞ 22
"""

def is_pal(num):

    if str(num)[0] == str(num)[-1]:
        return True

def closest_pal(num):

    if is_pal(num) == True:
        return num

    num_list = list(str(num))
    num_list[-1] = num_list[0]
    new_num = int(''.join(num_list))
    distance = abs(num - new_num)
    
    if is_pal(num-distance) == True:
        return num - distance
    else:
        return new_num

print(closest_pal(100))
print(closest_pal(27))
print(closest_pal(887))