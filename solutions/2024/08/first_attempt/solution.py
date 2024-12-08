#!/usr/bin/python3
import sys
from collections import defaultdict
from itertools import permutations

def addT(a, b):
    a1, a2 = a
    b1, b2 = b
    return (a1+b1, a2+b2)

def subT(a, b):
    a1, a2 = a
    b1, b2 = b
    return (a1-b1, a2-b2)

p1 = p2 = 0
inp = sys.argv[1]


rows = inp.strip().split("\n")
grid = defaultdict(lambda: None)
freqs = defaultdict(lambda: [])

for r, i in enumerate(rows):
    for c, j in enumerate(i):
        at = (r, c)
        grid[at] = j
        if j != ".":
            freqs[j].append(at)

for freq in freqs:
    if len(freqs[freq]) == 1:
        freqs.remove(freq)

antinodes1 = set()
antinodes2 = set()

for freq in freqs:
    trans = freqs[freq]
    for a1, a2 in permutations(trans, 2):
        antinodes2.add(a1)
        diff = subT(a1, a2)
        ant = addT(a1, diff)
        if ant in grid:
            antinodes1.add(ant)
        while ant in grid:
            antinodes2.add(ant)
            ant = addT(ant, diff)

p1 = len(antinodes1)
p2 = len(antinodes2)


print(p1, p2)