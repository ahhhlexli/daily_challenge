"""
A semiprime is a composite number that is the product of two primes. 
Apart from these two primes, its only other proper (non-self) divisor is 1.

The two prime factors of a semiprime can be the same number (e.g. the semiprime 49 is the product of 7x7). 
A semiprime that has two distinct prime factors is called a squarefree semiprime.

Create a function that takes a number and returns "Squarefree Semiprime", "Semiprime", or "Neither".

Examples
semiprime(49) ➞ "Semiprime"
semiprime(15) ➞ "Squarefree Semiprime"
semiprime(97) ➞ "Neither"
"""
import math

def find_factors(x):
    factors = []
    for i in range(2, x - 1):
       if x % i == 0:
           factors.append(i)
    return factors

def semiprime(num):

    sr = math.sqrt(num)
    factors = find_factors(num)
    if (int(sr) ** 2 == num):
        for i in range(1, int(sr/2)+1):
            if (sr % i) == 0:
                return 'Semiprime'

    if len(factors) == 0 or len(factors) > 2:
        return 'Neither'
    
    count = 0
    for factor in factors:
        for i in range(2, factor):
            for j in range(2, int(factor/2 + 1)):
                if i % j == 0:
                    count += 1
    if count == 2:
        return 'Squarefree Semiprime'



print(semiprime(49))
print(semiprime(15))
print(semiprime(97))
print(semiprime(663))