#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
from collections import deque
import heapq

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

addT = lambda a, b: (a[0] + b[0], a[1] + b[1])
subT = lambda a, b: (a[0] - b[0], a[1] - b[1])
magnT = lambda a: abs(a[0]) + abs(a[1])

p1 = p2 = 0
inp = sys.argv[1].strip()

path = set()
for r, row in enumerate(inp.split("\n")):
    for c, el in enumerate(row):
        if el == "#":
            continue
        at = (r, c)
        path.add(at)
        if el == "S":
            start = at
        elif el == "E":
            end = at

dists = {end: 0}
heap = [(0, end)]
seen = set()
while heap:
    score, at = heapq.heappop(heap)
    nscore = score + 1
    for d in directions:
        nat = addT(at, d)
        if nat in path and nat not in seen:
            heapq.heappush(heap, (nscore, nat))
            dists[nat] = nscore
            seen.add(nat)

uncheat = dists[start]

for cheat_start in path:
    for cheat_end in path:
        mag = magnT(subT(cheat_start, cheat_end))
        if mag <= 20:
            cheat_score = uncheat - dists[cheat_start] + dists[cheat_end] + mag
            saving = uncheat - cheat_score
            if saving >= 100:
                p2 += 1
                if mag <= 2:
                    p1 += 1

output(p1)
output(p2)