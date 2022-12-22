#!/usr/bin/env python3
import re

def first(grid, c = -1, r = -1, rev=1):
    if r != -1:
        for i in list(range(len(grid[r])))[::rev]:
            v = grid[r][i]
            if v != " ": return i, v
    else:
        for i in list(range(len(grid)))[::rev]:
            v = grid[i][c]
            if v != " ": return i, v
        

input = open("22_input").read()
#input = open("22_test").read()

input = input.split("\n\n")
grid_string, command = input[0], input[1]
command = command.strip()
grid = []

for y in grid_string.split("\n"):
    grid.append([])
    for x in y:
        grid[-1].append(x)

max_row = max(map(len, grid))
for y in grid:
    y += [" "] * (max_row - len(y))

i, f = first(grid, r=0)
x = i
y = 0
dir = 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] #ESWN
while command != "":
    print(x, y, dir)
    r = re.search("^\d+", command)
    if r:
        r = r.group(0)
        command = command.replace(r, "", 1)
        r = int(r)
        xm, ym = dirs[dir]
        while r:
            #print(r, x, y)
            x += xm
            y += ym
            if xm:
                if x >= len(grid[y]) or (xm == 1 and grid[y][x] == " "):
                    i, f = first(grid, r=y)
                    if f != "#":
                        x = i
                    else:
                        x -= xm
                        break
                elif x < 0 or (xm == -1 and grid[y][x] == " "):
                    i, l = first(grid, r=y, rev=-1)
                    if l != "#":
                        x = i
                    else:
                        x -= xm
                        break
            if ym:
                if y >= len(grid) or (ym == 1 and grid[y][x] == " "):
                    i, f = first(grid, c=x)
                    if f != "#":
                        y = i
                    else:
                        y -= ym
                        break
                elif y < 0 or (ym == -1 and grid[y][x] == " "):
                    i, l = first(grid, c=x, rev=-1)
                    if l != "#":
                        y = i
                    else:
                        y -= ym
                        break

            if grid[y][x] == "#":
                x -= xm
                y -= ym
                break

            r -= 1


    r = re.search("^[RL]", command)
    if r:
        r = r.group(0)
        command = command.replace(r, "", 1)
        if r == "R": dir = (dir + 1) % 4
        else: dir = (dir - 1) % 4

x += 1
y += 1
print(x, y, dir)
print(1000 * y + 4 * x + dir)
#57294 too low
#173158 too high