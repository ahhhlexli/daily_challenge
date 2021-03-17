"""Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.

Examples

next_prime(12) ➞ 13

next_prime(24) ➞ 29

next_prime(11) ➞ 11

11 is a prime, so we return the number itself.
"""

def next_prime(n):

    while True:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                break 
        else:
            return n
        n += 1

print(next_prime(12))
print(next_prime(24))
print(next_prime(11))