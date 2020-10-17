## Task: Write a program to calculate in how many ways you can pull 2 cards from a random deck of cards and get sum 13
## Approach: Used permutation to find all possible combinations and checked their sum if 13 or not
## Solution:
"""
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
## Author: Sampada Regmi
