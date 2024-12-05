#!/usr/bin/python3
import sys
from collections import defaultdict


p1 = p2 = 0
inp = sys.argv[1]

dirs = [(0,1),(1,1),(1,0),(1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]


def addTuple(a, b):
    a1, a2 = a
    b1, b2 = b
    return (a1+b1, a2+b2)

def multTuple(a, b):
    a1, a2 = a
    return (a1*b, a2*b)

rows = inp.strip().split("\n")
grid = defaultdict(lambda: None)

for r, i in enumerate(rows):
    for c, j in enumerate(i):
        grid[(r, c)] = j


want = "XMAS"

for r, i in enumerate(rows):
    for c, j in enumerate(i):
        for dir in dirs:
            for m in range(4):
                at = addTuple((r, c), multTuple(dir, m))
                if grid[at] != want[m]:
                    break
            else:
                p1 += 1


for r, i in enumerate(rows):
    for c, j in enumerate(i):
        at = (r, c)
        if grid[at] == "A":
            ul = grid[addTuple(at, (-1, -1))]
            ur = grid[addTuple(at, (-1, 1))]
            dl = grid[addTuple(at, (1, -1))]
            dr = grid[addTuple(at, (1, 1))]
            if (ul == "M" and dr == "S") or (ul == "S" and dr == "M"):
                if (ur == "M" and dl == "S") or (ur == "S" and dl == "M"):
                    p2 += 1



print(p1, p2)

