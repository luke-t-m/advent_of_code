#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
from collections import defaultdict
import heapq

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)

addT = lambda a, b: tuple(i + j for i, j in zip(a, b))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

p1 = p2 = 0
inp = sys.argv[1]

walls = set()
for r, row in enumerate(inp.split()):
    for c, sym in enumerate(row):
        at = (r, c)
        if sym == '#':
            walls.add(at)
        elif sym == 'S':
            start = at
        elif sym == 'E':
            end = at

def get_dists(origin, og_dir):
    # at, score, direction (int 0-3).
    heap = [(0, origin, og_dir)]
    dists_to = defaultdict(lambda: 10**100)
    while heap:
        score, at, straight = heapq.heappop(heap)
        if (at, straight) not in dists_to:
            dists_to[(at, straight)] = score
        else:
            continue
        left = (straight - 1) % 4
        right = (straight + 1) % 4
        nat = addT(at, directions[straight])
        if nat not in walls:
            heapq.heappush(heap, (score+1, nat, straight))
        for dir in [left, right]:
            heapq.heappush(heap, (score+1000, at, dir))
    return dists_to

dists_to = get_dists(start, 1)
p1 = 10**100
for dir in range(4):
    p1 = min(p1, dists_to[end, dir])

seen = set()
for dir in range(4):
    dists_two = get_dists(end, dir)
    for i in dists_to:
        at, dir = i
        ni = (at, (dir + 2) % 4)
        if dists_to[i] + dists_two[ni] == p1:
            seen.add(at)
p2 = len(seen)

output(p1)
output(p2)
