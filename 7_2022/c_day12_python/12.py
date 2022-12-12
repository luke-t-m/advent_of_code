#!/usr/bin/env python3

input = open("12_input").readlines()

def bfs(grid, start):
    queue = [(start, 0)]
    visited = set()
    while queue:
        pos, steps = queue.pop(0)
        if pos in visited: continue
        visited.add(pos)
        i, j = pos
        if grid[i][j] == '{':
            return steps
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = i + di, j + dj
            if (new_i >= 0 and new_i < len(grid) and
                new_j >= 0 and new_j < len(grid[0]) and
                ord(grid[new_i][new_j]) <= ord(grid[i][j]) + 1):
                queue.append(((new_i, new_j), steps + 1))


with open('12_input', 'r') as f:
    heightmap = [line.strip().replace("S", "a").replace("E", "{") for line in f.readlines()]

print(f"Part one: {bfs(heightmap, (0, 0))}")

outs = []
for x in range(len(heightmap[0])):
    for y in range(len(heightmap)):
        if heightmap[y][x] == "a":
            out = bfs(heightmap, (y, x))
            if out != None: outs.append(out)

print(f"Part two: {min(outs)}")

