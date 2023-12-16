from collections import deque
from operator import add


def make_grid(lines):
    return {(x, y): cell for y, row in enumerate(lines) for x, cell in enumerate(row)}


def reflect(direction, r):
    x, y = direction
    if y != 0:
        r = -r
    return ((0 - r) * y, r * x)


def solve(grid, start):
    queue = deque([start])
    seen = set()
    while len(queue) != 0:
        state = queue.pop()
        if state in seen:
            continue
        seen.add(state)
        at, direction = state
        n_at = tuple(map(add, at, direction))
        if n_at not in grid:
            continue
        dx, dy = direction
        what = grid[n_at]
        if what == "/":
            queue.append((n_at, reflect(direction, -1)))
        elif what == "\\":
            queue.append((n_at, reflect(direction, 1)))
        elif what == "|" and dx != 0:
            queue.append((n_at, (0, 1)))
            queue.append((n_at, (0, -1)))
        elif what == "-" and dy != 0:
            queue.append((n_at, (1, 0)))
            queue.append((n_at, (-1, 0)))
        else:
            queue.append((n_at, direction))
    return len(set([i[0] for i in seen])) - 1


with open("input") as file:
    raw = file.read()

lines = raw.strip().split("\n")

grid = make_grid(lines)

p1 = solve(grid, ((-1, 0), (1, 0)))

pos_starts = []
for y in range(len(lines)):
    pos_starts += [((-1, y), (1, 0)), ((len(lines[0]) + 1, y), (-1, 0))]
for x in range(len(lines[0])):
    pos_starts += [((x, -1), (0, 1)), ((len(lines) + 1, y), (0, -1))]

p2 = max(solve(grid, state) for state in pos_starts)

print(p1, p2)
