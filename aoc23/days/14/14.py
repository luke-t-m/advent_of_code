from copy import deepcopy
import numpy as np

with open("input") as file:
    raw = file.read()

if 0: raw = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

grid = [list(i) for i in raw.strip().split("\n")]
og = deepcopy(grid)
p1 = p2 = 0


def slide_up(grid):
    changes = 0
    for y in range(len(grid) - 1, 0, -1):
        for x in range(len(grid[0])):
            if grid[y][x] == "O" and grid[y-1][x] == ".":
                grid[y][x] = "."
                grid[y-1][x] = "O"
                changes += 1
    return changes


def print_grid():
    for row in grid:
        print("".join(row))


while (changes := slide_up(grid)) != 0:
    pass




p1 = sum(i * row.count("O") for i, row in enumerate(grid[::-1], 1))

seen = []
grid = og
skip = None
cycles = 0
while cycles != 1000000000:
    print(cycles)
    if skip != None and (cycles + 100 * skip < 1000000000):
        cycles += 100 * skip
        continue
    if skip != None and (cycles + skip < 1000000000):
        cycles += skip
        continue
    for i in range(4):
        while (changes := slide_up(grid)) != 0:
            pass
        grid = list([list(i) for i in zip(*grid[::-1])])

    if skip is None and grid in seen:
        o = seen.index(grid)
        skip = len(seen) - o
    seen.append(deepcopy(grid))
    p2 = sum(i * row.count("O") for i, row in enumerate(grid[::-1], 1))
    print(cycles, p2)
    cycles += 1

p2 = sum(i * row.count("O") for i, row in enumerate(grid[::-1], 1))
print(p1, p2)

