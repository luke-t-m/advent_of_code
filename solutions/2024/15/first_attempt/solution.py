#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
from collections import defaultdict, deque

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)

addT = lambda a, b: tuple(i + j for i, j in zip(a, b))

right = (0, 1)
left = (0, -1)
down = (1, 0)
up = (-1, 0)

directions = {'>': right,
              'v': down,
              '<': left,
              '^': up}

p1 = p2 = 0
inp = sys.argv[1]

inpgrid, instructions = inp.strip().split("\n\n")
instructions = [directions[sym] for sym in instructions if sym != '\n']

grid = defaultdict(lambda: None)
for r, row in enumerate(inpgrid.split('\n')):
    for c, el in enumerate(row):
        at = (r, c)
        if el == '@':
            guy = at
            grid[at] = '.'
        else:
            at = (r, c)
            grid[at] = el

grid2 = defaultdict(lambda: None)
for at in grid:
    r, c = at
    stuff = grid[at]
    nat = (r, c * 2)
    nat2 = (r, c * 2 + 1)
    if stuff == 'O':
        grid2[nat] = '['
        grid2[nat2] = ']'
    else:
        grid2[nat] = stuff
        grid2[nat2] = stuff
r, c = guy
guy2 = (r, c * 2)


for dir in instructions:
    new_guy = addT(guy, dir)
    at = new_guy
    while grid[at] == 'O':
        at = addT(at, dir)
    if grid[at] == '#':
        continue
    guy = new_guy
    grid[at] = 'O'
    grid[new_guy] = '.'

for at in grid:
    if grid[at] == 'O':
        r, c = at
        p1 += r * 100 + c


# part 2.
grid = grid2
guy = guy2

for dir in instructions:
    new_guy = addT(guy, dir)
    ats = deque([new_guy])
    to_move = set()
    seen = set()
    while len(ats) != 0:
        at = ats.pop()
        sym = grid[at]
        if sym == '#':
            break
        if sym == '.' or at in seen:
            continue
        if sym == '[':
            ats.append(addT(at, right))
        elif sym == ']':
            ats.append(addT(at, left))
        seen.add(at)
        to_move.add((at, sym))
        ats.append(addT(at, dir))
    else:
        guy = new_guy
        for at, _ in to_move:
            grid[at] = '.'
        for at, sym in to_move:
            grid[addT(dir, at)] = sym

for at in grid:
    if grid[at] == '[':
        r, c = at
        p2 += r * 100 + c

output(p1)
output(p2)