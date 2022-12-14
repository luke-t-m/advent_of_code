#!/usr/bin/env python3
import math
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
print(minw, minh)
width = maxw - minw
height = maxh - minh
grid = [['.'] * (width + 1) for ignored in range(height + 1)]


for line in input:
    line = line.split(" -> ")
    prev_point = list(map(int, line[0].split(",")))
    for point in line[1:]:
        point = list(map(int, point.split(",")))
        x = prev_point[0] - minw
        y = prev_point[1]- minh
        while x != point[0] - minw or y != point[1] - minh:
            grid[y][x] = "#"
            x = x + cmp((point[0] - minw), x) 
            y = y + cmp((point[1] - minh), y)
        grid[y][x] = "#"
        prev_point = point
grid[0 - minh][500 - minw] = "+"
for x in grid: print("".join(x))

# drop sand
#
for i in range(100000000):
    sx = 500 - minw
    sy = 0 - minh
    psx = sx
    psy = sy
    while True:
        if grid[sy + 1][sx] == ".":
            sy += 1
        elif grid[sy + 1][sx - 1] == ".":
            sy += 1
            sx -= 1
        elif grid[sy + 1][sx + 1] == ".":
            sy += 1
            sx += 1
        else:
            print("sand has stopped")
            break
    grid[sy][sx] = "o"
    print(i+1)

#for x in grid: print("".join(x))