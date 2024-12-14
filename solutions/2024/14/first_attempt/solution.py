#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
import regex as re

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)


p1 = p2 = 0
inp = sys.argv[1]

def addT(a, b):
    a1, a2 = a
    b1, b2 = b
    return (a1+b1, a2+b2)


grid_width = 101
grid_height = 103
steps = 100

half_width = grid_width // 2
half_height = grid_height // 2

ne = se = sw = nw = 0

for nums in re.findall("p=(-?\d*),(-?\d*) v=(-?\d*),(-?\d*)", inp):
    x, y, xm, ym = map(int, nums)
    fx = (x + (xm * steps)) % grid_width
    fy = (y + (ym * steps)) % grid_height
    if fx == half_width or fy == half_height:
        continue
    if fx < half_width:
        if fy < half_height:
            nw += 1
        else:
            sw += 1
    else:
        if fy < half_height:
            ne += 1
        else:
            se += 1

p1 = ne * se * sw * nw

# part two.
robots = []
for nums in re.findall("p=(-?\d*),(-?\d*) v=(-?\d*),(-?\d*)", inp):
    robots.append(list(map(int, nums)))

for step in range(1, 10000):
    robots_at = set()
    for i, robot in enumerate(robots):
        x, y, xm, ym = robot
        fx = (x + xm) % grid_width
        fy = (y + ym) % grid_height
        robots[i][0] = fx
        robots[i][1] = fy
        robots_at.add((fx, fy))
    print(f"\n\n\n\n{step}")
    for x in range(grid_width):
        print()
        for y in range(grid_height):
            at = (x, y)
            if at in robots_at:
                print("█", end="")
            else:
                print(".", end="")
    




output(p1)
output(p2)