#!/usr/bin/python3
import sys
from collections import defaultdict

p1 = p2 = 0
inp = sys.argv[1]

dirs = [(-1,0),(0, 1),(1, 0),(0, -1)]

def addTuple(a, b):
    a1, a2 = a
    b1, b2 = b
    return (a1+b1, a2+b2)

rows = inp.strip().split("\n")
grid = defaultdict(lambda: None)

grid2 = grid.copy()

for r, i in enumerate(rows):
    for c, j in enumerate(i):
        if j == "^":
            guard = (r, c)
            grid[(r, c)] = "X"
        else:
            grid[(r, c)] = j

at = guard
dir = 0
while True:
    nat = addTuple(at, dirs[dir])
    if nat not in grid:
        break
    if grid[nat] not in ".X":
        dir = (dir + 1) % 4
    else:
        grid[nat] = "X"
        at = nat

pos_obs = []
for k in grid:
    if grid[k] == "X":
        p1 += 1
        pos_obs.append(k)

old_ob = (-1000000, -1000000)
for ob in pos_obs:
    grid[ob] = "M"
    grid[old_ob] = "X"
    old_ob = ob
    dir = 0
    at = guard
    seen = set([(at, 0)])
    lens = 0
    while True:
        nat = addTuple(at, dirs[dir])
        if nat not in grid:
            break
        if (nat, dir) in seen:
            p2 += 1
            break
        if grid[nat] not in ".X":
            dir = (dir + 1) % 4
        else:
            seen.add((nat, dir))
            at = nat



print(p1, p2)