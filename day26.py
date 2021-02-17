"""
Create a function that takes a list and returns a new list containing only prime numbers.

Examples

filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]

filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]

filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]
"""

def return_prime(l):

    answer = []

    for i in l:
        for num in range(2,(i//2 + 1)):
            if i % num == 0:
                break 
        else:
            if i == 1:
                pass 
            else: 
                answer.append(i)
                
    return answer


print(return_prime([7, 9, 3, 9, 10, 11, 27]))
print(return_prime([10007, 1009, 1007, 27, 147, 77, 1001, 70]))
print(return_prime([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]))