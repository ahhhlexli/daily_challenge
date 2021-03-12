"""There are two players, Alice and Bob, each with a 3-by-3 grid. 
A referee tells Alice to fill out one particular row in the grid (say the second row) by putting either a 1 or a 0 in each box, 
such that the sum of the numbers in that row is odd. The referee tells Bob to fill out one column in the grid (say the first column) 
by putting either a 1 or a 0 in each box, such that the sum of the numbers in that column is even.

Alice and Bob win the game if Alice’s numbers give an odd sum, Bob’s give an even sum, 
and (most important) they’ve each written down the same number in the one square where their row and column intersect.

Examples
magic_square_game([2, "100"], [1, "101"]) ➞ False
magic_square_game([2, "001"], [1, "101"]) ➞ True
magic_square_game([3, "111"], [2, "011"]) ➞ True
magic_square_game([1, "010"], [3, "101"]) ➞ False

Two lists, Alice [row, "her choice"], Bob [column, "his choice"]"""

import numpy as np

def magic_square_game(l1, l2):

    ann_grid = np.full((3,3), 5, dtype=int)
    ann_row = l1[0] - 1
    ann_vals = [i for i in str(l1[1])]
    bob_col = l2[0] - 1
    bob_vals = [i for i in str(l2[1])]
    ann_grid[ann_row] = ann_vals
    #print(ann_grid)
    for i in range(3):
        if ann_grid[:, bob_col][i] == float(bob_vals[i]):
            return True
    return False


print(magic_square_game([2, "100"], [1, "101"]))
print(magic_square_game([2, "001"], [1, "101"]))
print(magic_square_game([3, "111"], [2, "011"]))
print(magic_square_game([1, "010"], [3, "101"]))