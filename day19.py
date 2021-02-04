""" 
Given a string of names with a certain pattern, return a formatted string with a certain pattern. 

Example:
Input:
"Alfred:Black;Carey:Drake;Elena:Ferguson;Georgina:Harrison"

Output:
"(BLACK, ALFRED)(DRAKE, CAREY)(FERGUSON, ELENA)(HARRISON, GEORGINA)"
"""

def string_returner(string):

    pairs = string.upper().split(';')
    pairs = [('(' + str(i.split(':')[1]) + ' , ' + str(i.split(':')[0]) + ')') for i in pairs]
    answer = ''
    for i in pairs:
        answer += i

    return answer

print(string_returner('Alfred:Black;Carey:Drake;Elena:Ferguson;Georgina:Harrison'))