""" 
Given the number of people in the room, 
calculate the probability that any two people in that room have the same birthday, 
assuming we have 365 days in a year. (no leap years) 
Return the probability rounded off to two decimal points.
"""

import math

def calculate_probability(n):

    #probability no one shares birthday 
    """365! / (365-n)! * 365 ^ n"""
    prob_not = math.factorial(365) / (math.factorial(365-n) * 365**n)
    probability = 1- prob_not


    return probability

print(calculate_probability(20))
