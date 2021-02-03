"""Given an integer greater than 0, return a list of all possible palindromes of the integer.
Example:

Input: 
34322122

Output:
[22, 212, 343, 22122]
"""

def number_pal(number):

    number = list(str(number))
    pal_list = []

    for i in range(1, len(number)-1):

        if number[i-1] == number[i]:
            pal_list.append(int(''.join(number[i-1:i+1])))
        
        for j in range(1, len(number)//2):
            try:
                if number[i-j] == number[i+j]:
                    print(int(''.join(number[i-j:i+j+1])))
                    pal_list.append(int(''.join(number[i-j:i+j+1])))
                else:
                    break
            except:
                pass
            
    return pal_list 

print(number_pal(34322122))