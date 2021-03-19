"""
A prison can be represented as a list of cells. Each cell contains exactly one prisoner. 
A 1 represents an unlocked cell and a 0 represents a locked cell.

[1, 1, 0, 0, 0, 1, 0] Starting from the leftmost cell, 
you are tasked with seeing how many prisoners you can set free, with a catch. 
Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again.

So, if we use the example above:
[1, 1, 0, 0, 0, 1, 0] 
You free the prisoner in the 1st cell.
[0, 0, 1, 1, 1, 0, 1] 
You free the prisoner in the 3rd cell (2nd one locked).
[1, 1, 0, 0, 0, 1, 0]
You free the prisoner in the 6th cell (3rd, 4th and 5th locked).
[0, 0, 1, 1, 1, 0, 1]

You free the prisoner in the 7th cell - and you are done!
Here, we have freed 4 prisoners in total.

Create a function that, given this unique prison arrangement, returns the number of freed prisoners.

Examples

freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4
freed_prisoners([1, 1, 1]) ➞ 1
freed_prisoners([0, 0, 0]) ➞ 0
freed_prisoners([0, 1, 1, 1]) ➞ 0
"""

def freed_prisoners(l):

    count = 0

    if l[0] == 0:
        return 0

    for i in range(len(l)):
        if l[i] == 1:
            count += 1
            l = [0 if l[j] == 1 else 1 for j in range(len(l))]
        
    return count
    
print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))
print(freed_prisoners([1, 1, 1]))
print(freed_prisoners([0, 0, 0]))
print(freed_prisoners([0, 1, 1, 1]))