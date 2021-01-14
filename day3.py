""" 
Create a function that calculates how many times an integer can be divided 
by another given integer. If the answer of resulting divisions does not 
result in an integer, that division is not counted towards the number of times. As an example: 

If n is 10 and divisor is 3, since in the first division 10/3 doesn't return an integer, 
this division doesn't count towards the number of times and therefore its number of times should be 0.
"""

def division(n, divisor):
    count = 0
    if divisor == 1:
        return "Error - divisor is 1"
    else:
        while n % divisor == 0:
            n = n / divisor
            count += 1
    return count

print(division(1000000000,2))
