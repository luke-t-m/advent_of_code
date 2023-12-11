with open("input") as file:
    raw = file.read()


lines = raw.strip().split("\n")
p1 = p2 = 0


def expand(grid):
    new_grid = []
    for row in grid:
        new_grid.append(row)
        if all([i == "." or i == "V" for i in row]):
            new_grid.append("V" * len(grid[0]))
    return new_grid


def tranpose(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]


grid = expand(lines)
grid = tranpose(grid)
grid = expand(grid)
grid = tranpose(grid)

stars = []
for y, row in enumerate(grid):
    for x, at in enumerate(row):
        if at == "#":
            stars.append((x, y))
stars.sort()


pairs = [(a, b) for idx, a in enumerate(stars) for b in stars[idx + 1 :]]


big_empty = 1000000 - 2
for a, b in pairs:
    xa, ya = a
    xb, yb = b
    p1 += abs(xb - xa) + abs(yb - ya)
    for x in range(min(xa, xb), max(xa, xb)):
        if grid[0][x] == "V":
            p2 += big_empty
    for y in range(min(ya, yb), max(ya, yb)):
        if grid[y][0] == "V":
            p2 += big_empty

p2 = p2 + p1
print(p1, p2)
