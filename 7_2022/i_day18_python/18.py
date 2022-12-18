#!/usr/bin/env python3

def add_three(x, y):
    a, b, c = x
    d, e, f = y
    return [a+d, b+e, c+f]

input = open("18_input").readlines()
cubes = [list(map(int, x.strip().split(","))) for x in input]
mods = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
p1, p2 = 0, 0

for c in cubes:
    sides = 6
    for m in mods:
        if add_three(c, m) in cubes: sides -= 1
    p1 += sides

ax = [x[0] for x in cubes]
maxx, mix = max(ax) + 1, min(ax) - 1
ay = [x[1] for x in cubes]
may, miy = max(ay) + 1, min(ay) - 1
az = [x[2] for x in cubes]
maz, miz = max(az) + 1, min(az) - 1

stack = [[mix, miy, miz]]
visited = []
while stack:
    if len(stack) % 50 == 0: print(f"in stack: {len(stack)} ", end = "\r")
    a = stack.pop(0)
    x, y, z = a
    if x > maxx or x < mix or y > may or y < miy or z > maz or z < miz or a in visited: continue
    visited.append(a)
    for m in mods:
        b = add_three(a, m)
        if b in cubes: p2 += 1
        else: stack.append(b)
print(f"in stack: {len(stack)} \nPart one: {p1}\nPart two: {p2}")
