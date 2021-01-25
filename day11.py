""" 
Given a string, return the character with the most value. 
The value of a character is the difference between the index of its 
first occurrence and the index of its last occurrence. 
If there is a tie, return the character that goes first alphabetically.

Example:
Input: 'abcdbcd'

Output: 'b', since difference between first index and last index = 4 - 1 = 3, 
which ties with the values of c and d but since b goes first alphabetically, 
that's the most valuable character.
""" 
import re
def max_value(text):

    str_set = set(text)
    most_val = None
    max_val = 0
    for letter in str_set:
        first = text.find(letter)
        last = text.rfind(letter)
        dif = last - first
        if dif >= max_val and dif != 0:
            max_val = dif
            if most_val == None:
                most_val = letter
            if dif > max_val:
                most_val = letter
            else:
                current = [most_val, letter]
                most_val = sorted(current)[0]

    return most_val
print(max_value('abcdbcd'))
