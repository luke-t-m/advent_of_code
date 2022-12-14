#!/usr/bin/env python3
import math
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy

def cmp(a, b):
    return (a > b) - (a < b)

input = open("14_input").readlines()
#input = open("14_test").readlines()

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
for x in grid: print("".join(map(str, x)))

# drop sand

frames = []
sy = 0
sx = 0
mod = 0
sand = 0
while True:
    frames.append(deepcopy(grid))
    sx = (500 - minw) + mod
    sy = 0 - minh
    while True:
        if sx <= 0:
            grid = [[0] + x for x in grid]
            mod += 1
            break
        elif sx >= len(grid[0]) - 1:
            grid = [x + [0] for x in grid]
            break
        elif sy >= len(grid) - 1:
            grid[sy][sx] = 3
            break
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
            sand += 1
            break
    if sx == (500 - minw) + mod and sy == 0 - minh: break
print(sand)

fig, ax = plt.subplots()

ims = []
for i in frames:
    im = plt.imshow(i, animated = True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

ani.save("input_animation.mp4")
plt.show()