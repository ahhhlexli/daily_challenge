"""Given a list of 11 integers, return a string in the form of a 
Hong Kong phone number in this format: +852 xxxx xxxx

Only the numbers 2, 3, 5, 6, 7, and 9 can be added after the extension 852.

Example 1:

Input:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]

Returns:
"+852 9134 6701"
"""
import random 

def phone_number(num_list):

    extension = [8, 5, 2]
    phone = '+'

    for number in extension:
        if number in num_list:
            num_list.remove(number)
            phone += str(number)
        else:
            return 'Invalid List'
    phone += ' '

    after_ext = [2, 3, 5, 6, 7, 9]

    for num in after_ext:
        if num in num_list:
            num_list.remove(num)
            phone += str(num)
            break
    
    remove_list = num_list.copy()
    for i in range(len(num_list)):
        if len(phone) == 9:
            phone += ' '
        next_num = random.choice(remove_list)
        phone += str(next_num)
        remove_list.remove(next_num)

    return phone

print(phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]))