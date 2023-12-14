from copy import deepcopy


def slide_up(grid):
    changed = True
    while changed:
        changed = False
        for y in range(len(grid) - 1, 0, -1):
            for x in range(len(grid[0])):
                if grid[y][x] == "O" and grid[y - 1][x] == ".":
                    grid[y][x] = "."
                    grid[y - 1][x] = "O"
                    changed = True


def rotated(grid):
    return list([list(i) for i in zip(*grid[::-1])])


def score(grid):
    return sum(i * row.count("O") for i, row in enumerate(grid[::-1], 1))


with open("input") as file:
    raw = file.read()

grid = [list(i) for i in raw.strip().split("\n")]
slide_up(grid)
p1 = score(grid)

seen = []
grid = [list(i) for i in raw.strip().split("\n")]
want = 1000000000
while True:
    for _ in range(4):
        slide_up(grid)
        grid = rotated(grid)

    if grid in seen:
        loop_start = seen.index(grid)
        loop_len = len(seen) - loop_start
        grid = seen[loop_start + ((want - loop_start) % loop_len) - 1]
        break
    seen.append(deepcopy(grid))

p2 = score(grid)
print(p1, p2)
