#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy

DO_ANIMATION = True

# 0 = "."
# 1 = "#"
# 2 = "+"
# 3 = "o"

def cmp(a, b):
    return (a > b) - (a < b)

filename = "14_test"
input = open(filename).readlines()

minw, maxw, minh, maxh = math.inf, 0, math.inf, 0
for line in input:
    line = line.split(" -> ")
    line = [x.split(",") for x in line]
    line = list(map(lambda x: list(map(int, x)), line))
    for point in line + [[500, 0]]:
        maxw = max(point[0], maxw)
        minw = min(point[0], minw)
        maxh = max(point[1], maxh)
        minh = min(point[1], minh)
width = maxw - minw
height = maxh - minh
floor = maxh + 2

grid = [[0] * (width + 1) for ignored in range(floor + 1)]

for line in input:
    line = line.split(" -> ")
    prev_point = list(map(int, line[0].split(",")))
    for point in line[1:]:
        point = list(map(int, point.split(",")))
        x = prev_point[0] - minw
        y = prev_point[1]- minh
        while x != point[0] - minw or y != point[1] - minh:
            grid[y][x] = 1
            x = x + cmp((point[0] - minw), x) 
            y = y + cmp((point[1] - minh), y)
        grid[y][x] = 1
        prev_point = point
grid[0 - minh][500 - minw] = 2
#for x in grid: print("".join(map(str, x)))

# drop sand
if DO_ANIMATION: frames = []

def drop_sand(grid, p2 = False):
    grid = deepcopy(grid)
    sx, sy, mod, sands = 0, 0, 0, 0
    while True:
        sx, sy = (500 - minw) + mod, 0 - minh
        if DO_ANIMATION and p2: frames.append(deepcopy(grid))
        while True:
            if sx <= 0:
                if p2:
                    grid = [[0] + x for x in grid]
                    mod += 1
                    break
                else: return sands
            elif sx >= len(grid[0]) - 1:
                if p2:
                    grid = [x + [0] for x in grid]
                    break
                else: return sands
            elif sy >= len(grid) - 1:
                if p2:
                    grid[sy][sx] = 3
                    break
                else: return sands
            elif grid[sy + 1][sx] == 0:
                sy += 1
            elif grid[sy + 1][sx - 1] == 0:
                sy += 1
                sx -= 1
            elif grid[sy + 1][sx + 1] == 0:
                sy += 1
                sx += 1
            else:
                grid[sy][sx] = 3
                sands += 1
                break
        if sx == (500 - minw) + mod and sy == 0 - minh: return sands

print(f"Part one: {drop_sand(grid)}")
print(f"Part two: {drop_sand(grid, True)}")

if DO_ANIMATION:
    fig, ax = plt.subplots()

    ims = []
    for i in frames:
        im = plt.imshow(i, animated = True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

    ani.save(filename + "_animation.mp4")
    plt.show()