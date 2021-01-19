"""Given a list of integers, create a function that finds the odd one out in the list."""

def odd_one_out(input_list):

    uniques = set(input_list)
    for i in uniques:
        if input_list.count(i) == 1:
            return i

print(odd_one_out([1,1,1,1,1,1,1,2]))
