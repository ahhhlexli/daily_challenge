""" 
A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. Create a function that returns True if a string is an almost-palindrome and False otherwise.

Examples

almost_palindrome("abcdcbg") ➞ True
#Transformed to "abcdcba" by changing "g" to "a".

almost_palindrome("abccia") ➞ True
#Transformed to "abccba" by changing "b" to "a".

almost_palindrome("abcdaaa") ➞ False
#Can't be transformed to a palindrome in exactly 1 turn.

almost_palindrome("1234312") ➞ False
"""
import string

def almost_pal(s1):

    if s1 == s1[::-1]:
        return True 
    else:
        for i in range(len(s1)):
            for j in string.ascii_letters:
                s2 = list(s1)
                s2[i] = j
                s3 = ''.join(s2)
                if s3 == s3[::-1]:
                    return True 
        if s1 != s1[::-1]:
            return False

print(almost_pal('abcdcbg'))