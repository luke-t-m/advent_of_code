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


p1 = p2 = 0
inp = sys.argv[1]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_checks = {(0, 1): (1, 0), (0, -1): (1, 0), (1, 0): (0, 1), (-1, 0): (0, 1)}

rows = inp.strip().split("\n")
letgrid = defaultdict(lambda: None)
regions = defaultdict(lambda: [])

for r, i in enumerate(rows):
    for c, val in enumerate(i):
        at = (r, c)
        letgrid[at] = val

id = 0
seen = set()
for r, _ in enumerate(rows):
    for c, _ in enumerate(i):
        at = (r, c)
        if at in seen:
            continue
        dq = deque([at])
        region = set([at])
        while dq:
            at = dq.pop()
            if at in seen:
                continue
            for dir in dirs:
                nat = addT(at, dir)
                if letgrid[nat] == letgrid[at]:
                    region.add(nat)
                    dq.append(nat)
                    seen.add(at)
        if len(region) != 0:
            regions[id] = region
            id += 1

for id in regions:
    per = per2 = 0
    for at in regions[id]:
        for dir in dirs:
            if letgrid[addT(at, dir)] != letgrid[at]:
                per += 1
                check = dir_checks[dir]
                checked = addT(at, check)
                if (letgrid[checked] != letgrid[at] or letgrid[addT(checked, dir)] == letgrid[at]):
                    per2 += 1
    lr = len(regions[id])
    p1 += per * lr
    p2 += per2 * lr

output(p1)
output(p2)