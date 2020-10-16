from itertools import permutations
from pprint import pprint
Deck = [i for i in range(1, 13+1)]
possibilities = 0
possibility = []
for i in range(4):
    p = permutations(Deck, 2)
    for x,y in p:
        if x+y == 13:
            possibilities += 1
            possibility.append(tuple([x,y]))
print("List of Possibilities: ")
pprint(possibility)
print(f'There are {possibilities} possibilities')

"""
Output:
List of Possibilities: 
[(1, 12),
 (2, 11),
 (3, 10),
 (4, 9),
 (5, 8),
 (6, 7),
 (7, 6),
 (8, 5),
 (9, 4),
 (10, 3),
 (11, 2),
 (12, 1),
 (1, 12),
 (2, 11),
 (3, 10),
 (4, 9),
 (5, 8),
 (6, 7),
 (7, 6),
 (8, 5),
 (9, 4),
 (10, 3),
 (11, 2),
 (12, 1),
 (1, 12),
 (2, 11),
 (3, 10),
 (4, 9),
 (5, 8),
 (6, 7),
 (7, 6),
 (8, 5),
 (9, 4),
 (10, 3),
 (11, 2),
 (12, 1),
 (1, 12),
 (2, 11),
 (3, 10),
 (4, 9),
 (5, 8),
 (6, 7),
 (7, 6),
 (8, 5),
 (9, 4),
 (10, 3),
 (11, 2),
 (12, 1)]
There are 48 possibilities
"""
