"""Given two integer inputs n and d,
 create a function that squares all numbers from 1 to n, 
 then returns the count of all instances of d from the square results.
 
n: 5
d: 1
square of numbers from 1 to 5: 1, 4, 9, 16, 25
returns: 2 (since there's 2 instances of the digit 1, in 1 and 16)"""

def instance_in_square(n, d):

    return ''.join([str(i**2) for i in range(1, n+1)]).count(str(d))

print(instance_in_square(5, 1))

