#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
from collections import defaultdict
import heapq

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)

addT = lambda a, b: (a[0] + b[0], a[1] + b[1])

GOOD = 0
CORRUPTED = 1

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

p1 = p2 = 0
inp = sys.argv[1].strip()
lines = inp.split("\n")

grid_w = grid_h = 71
grid = defaultdict(lambda: CORRUPTED)

for r in range(grid_h):
    for c in range(grid_w):
        grid[(r, c)] = GOOD

for line in lines:
    r, c = line.split(",")
    r = int(r)
    c = int(c)
    grid[(r, c)] = CORRUPTED

for line in lines[::-1]:
    r, c = line.split(",")
    r = int(r)
    c = int(c)
    grid[(r, c)] = GOOD
    heap = [(0, (0, 0))]
    seen = set()
    while len(heap) > 0:
        score, at = heapq.heappop(heap)
        for direction in directions:
            nat = addT(at, direction)
            nscore = score + 1
            if nat == (grid_w-1, grid_h-1):
                break
            if grid[nat] != CORRUPTED and nat not in seen:
                heapq.heappush(heap, (nscore, nat))
                seen.add(nat)
        else:
            continue
        break
    else:
        continue
    p2 = f"{r},{c}"
    break

heap = [(0, (0, 0))]
seen = set()
while len(heap) > 0:
    score, at = heapq.heappop(heap)
    for direction in directions:
        nat = addT(at, direction)
        nscore = score + 1
        if nat == (grid_w-1, grid_h-1):
            p1 = nscore
            break
        if grid[nat] != CORRUPTED and nat not in seen:
            heapq.heappush(heap, (nscore, nat))
            seen.add(nat)
    else:
        continue
    break



output(p1)
output(p2)