"""Given any number, we can create a new number by adding the sums of squares of digits of that number. 
For example, given 203, our new number is 4 + 0 + 9 = 13. If we repeat this process, we get a sequence of numbers:

203 -> 13 -> 10 -> 1 -> 1 Sometimes, like with 203, the sequence reaches (and stays at) 1. Numbers like this are called happy.

Not all numbers are happy. If we started with 11, the sequence would be:

11 -> 2 -> 4 -> 16 -> ... This sequence will never reach 1, and so the number 11 is called unhappy.

Given a positive whole number, you have to determine whether that number is happy or unhappy.

Examples

happy(203) ➞ True
happy(11) ➞ False
happy(107) ➞ False
"""

def happy(n):

    path = []
    while n not in path:
        path.append(n)
        if n == 1:
            return True
        else:
            numbers = [int(i) for i in list(str(n))]
            n = sum([i**2 for i in numbers])
    return False
    



    

    

print(happy(203))
print(happy(11))
print(happy(107))

