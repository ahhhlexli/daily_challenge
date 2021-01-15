"""Create a function that given an n positive integer, it sums all the cubed values from 1 to n. Return the sum."""

def sum_cubes(n):

    answer = 0
    for i in range(1, n+1):
        answer += i**3

    return answer 

print(sum_cubes(5))

