""" 
Given a string, count all the lowercase letters. 
Return a dictionary with the keys as the lowercase letters 
and the values as the letters' counts respectively. 
The keys should be sorted in alphabetical order.
Example:

Input:
"apple"

Output:
{'a': 1, 'e': 1, 'l': 1, 'p': 2}
"""

def dict_counter(string):

    return {letter: string.count(letter) for letter in sorted(set(string))}

print(dict_counter('apple'))