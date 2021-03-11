""" 
Standard competition ranking (also known as "1224" ranking) assigns the same rank to matching values. 
Rank numbers are increased each time, so ranks are sometimes skipped. 
If we have 5 scores (the highest score having a rank of 1):

No matching values:
Scores = [99, 98, 97, 96, 95] Rank = 1, 2, 3, 4, 5 
With matching values:
Scores = [99, 98, 98, 96, 95] Rank = 1, 2, 2, 4, 5

Second and third scores are equal, so rank "3" is skipped.
Given a dictionary containing the names and scores of 5 competitors, and a competitor name, 
return the rank of that competitor after applying competition ranking.

Examples
competition_rank({ "George": 96, "Emily": 95, "Susan": 93, "Jane": 89, "Brett": 82 }, "Jane") ➞ 4
competition_rank({ "Kate": 92, "Carol": 92, "Jess": 87, "Bruce": 87, "Scott": 84 }, "Bruce") ➞ 3
"""

def competition_rank(score_dict, name):

    scores = sorted(list(score_dict.values()), reverse=True)
    ranks = {}
    for i in range(0, len(scores)):
        previous = scores[i-1]
        if scores[i] == previous:
            ranks[scores[i]] = i
        else:
            ranks[scores[i]] = i+1
    return ranks[score_dict[name]]

print(competition_rank({ "George": 96, "Emily": 95, "Susan": 93, "Jane": 89, "Brett": 82 }, "Jane"))
print(competition_rank({ "Kate": 92, "Carol": 92, "Jess": 87, "Bruce": 87, "Scott": 84 }, "Bruce"))