"""
Given a string, add or subtract numbers and return the answer.
Example:
Input: 1plus2plus3minus4
Output: 2
Input: 2minus6plus4plus7
Output: 7"""

def calc(string):
    
    string = string.replace('plus', ' + ').replace('minus', ' - ')
    
    return eval(string)

