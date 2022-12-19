#!/usr/bin/env python3
from math import inf
from collections import deque

def add_three(x, y):
    a, b, c = x
    d, e, f = y
    return (a+d, b+e, c+f)

input = open("18_input").readlines()

cubes = set([tuple([int(y) for y in x.split(",")]) for x in input])
mods = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
p1, p2 = len(cubes) * 6, 0

minx, miny, minz, maxx, maxy, maxz = inf, inf, inf, -inf, -inf, -inf
for c in cubes:
    x, y, z = c
    minx = min(x, minx)
    maxx = max(x, maxx)
    miny = min(y, miny)
    maxy = max(y, maxy)
    minz = min(z, minz)
    maxz = max(z, maxz)
    for m in mods:
        if add_three(c, m) in cubes: p1 -= 1

minx -= 1
miny -= 1
minz -= 1
maxx += 1
maxy += 1
maxz += 1

queue = deque([(minx, miny, minz)])
visited = set()
while queue:
    a = queue.popleft()
    for m in mods:
        b = add_three(a, m)
        x, y, z = b
        if x > maxx or x < minx or y > maxy or y < miny or z > maxz or z < minz: continue
        elif b in cubes: p2 += 1
        elif b not in visited:
            queue.append(b)
            visited.add(b)

print(f"Part one: {p1}\nPart two: {p2}")
