"""Given a string, create a function that splits the string into pairs 
of two characters. Put the pairs inside a list then return the list. 
If a character is missing in a pair, use the character '?' 
to replace the missing character.

Example:
Input: "abcdefg"
Output = ["ab", "cd", "ef", "g?"]

Input: "abcdef"
Output = ["ab", "cd", "ef"]
"""

def string_splitter(string):

    pairs = [string[i:i+2] for i in range(0, len(string), 2)]
    
    if len(pairs[-1]) == 1:
        pairs[-1] += '?'

    return pairs

print(string_splitter('abcdefg'))
print(string_splitter("abcdef"))