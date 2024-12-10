#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
from collections import defaultdict, deque


def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)

def addT(a, b):
    a1, a2 = a
    b1, b2 = b
    return (a1+b1, a2+b2)

inp = sys.argv[1]
p1 = p2 = 0

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

rows = inp.strip().split("\n")
grid = defaultdict(lambda: None)
trailheads = []

for r, i in enumerate(rows):
    for c, j in enumerate(i):
        at = (r, c)
        val = int(j)
        grid[at] = val
        if val == 0:
            trailheads.append(at)


for th in trailheads:
    dq = deque([th])
    seen = set()
    while dq:
        at = dq.pop()
        if at in seen:
            continue
        seen.add(at)
        val = grid[at]
        want = val + 1
        if val == 9:
            p1 += 1
            continue
        for dir in dirs:
            next = addT(at, dir)
            if want == grid[next]:
                dq.append(next)

for th in trailheads:
    dq = deque([th])
    while dq:
        at = dq.pop()
        val = grid[at]
        want = val + 1
        if val == 9:
            p2 += 1
            continue
        for dir in dirs:
            next = addT(at, dir)
            if want == grid[next]:
                dq.append(next)


output(p1)
output(p2)