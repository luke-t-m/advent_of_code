from collections import deque

DIRECTIONS = {">": (1, 0), "^": (0, -1), "<": (-1, 0), "v": (0, 1)}
dfs_seen = set()


def make_grid(ls):
    return {(x, y): c for y, r in enumerate(ls) for x, c in enumerate(r) if c != "#"}


def tup_add(tup1, tup2):
    return tuple(i + j for (i, j) in zip(tup1, tup2))


def find_costs(grid, start, goals, is_p2=False):
    seen = set()
    reached = dict()
    queue = deque([(start, 0)])
    while len(queue) != 0:
        at, cost = queue.pop()
        if at in seen or at not in grid:
            continue
        if at in goals and at != start:
            reached[at] = cost
            continue
        seen.add(at)
        what = grid[at]
        if what == "." or (is_p2 and what in DIRECTIONS):
            for dir in DIRECTIONS.values():
                queue.append((tup_add(at, dir), cost + 1))
        elif what in DIRECTIONS:
            queue.append((tup_add(at, DIRECTIONS[what]), cost + 1))
    return reached


def dfs(at, finish):
    best = - 2 ** 100
    if at == finish:
        return 0
    dfs_seen.add(at)
    for next, move_cost in paths[at].items():
        if next not in dfs_seen:
            best = max(best, dfs(next, finish) + move_cost)
    dfs_seen.remove(at)

    return best


with open("23/input") as file:
    raw = file.read()

lines = raw.strip().split("\n")
grid = make_grid(lines)
start = (lines[0].index("."), 0)
finish = (lines[-1].index("."), len(lines) - 1)

nodes = {
    at: c for at, c in grid.items()
    if sum(1 for d in DIRECTIONS.values() if tup_add(at, d) in grid) not in [0, 2]
}

paths = {i: find_costs(grid, i, nodes) for i in nodes}
p1 = dfs(start, finish)

paths = {i: find_costs(grid, i, nodes, True) for i in nodes}
p2 = dfs(start, finish)

print(p1, p2)
