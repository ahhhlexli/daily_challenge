"""
Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.

Examples

censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*") ➞ "The *** jumped **** the moon."

censor_string("Why did the chicken cross the road?", ["did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
"""

def censor_string(string, words, char):

    string = string.split()
    for i in range(len(string)):
        if string[i] in words:
            string[i] = char * len(string[i])

    return ' '.join(string)

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road?", ["did", "chicken", "road"], "*"))
