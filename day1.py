"""Create a function that removes all capital letters and punctuation in a string. Return the clean string."""

import string

def clean_string(s):

    for i in s:
        if i.isupper() or i in string.punctuation:
            s = s.replace(i, '')

    return s

print(clean_string('HELLO hello hi bye (*)^*&^(*&^(*&^ABCDefg!'))