import heapq

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def make_grid(lines):
    return {
        (x, y): int(cell) for y, row in enumerate(lines) for x, cell in enumerate(row)
    }


def solve(grid, start, goal, min_move, max_move):
    seen = set()
    queue = [(0, start, None, 0)]
    heapq.heapify(queue)

    while len(queue) != 0:
        cost, at, dir, consec = heapq.heappop(queue)

        if at == goal and consec >= min_move:
            return cost

        state = (at, dir, consec)
        if state in seen:
            continue
        seen.add(state)
        if dir is not None and consec < max_move:
            n_at = tuple(i + j for (i, j) in zip(at, dir))
            if n_at in grid:
                heapq.heappush(queue, (cost + grid[n_at], n_at, dir, consec + 1))
        if consec >= min_move or dir is None:
            for dir2 in DIRECTIONS:
                if dir2 == dir or dir == (-dir2[0], -dir2[1]):
                    continue
                n_at = tuple(i + j for (i, j) in zip(at, dir2))
                if n_at in grid:
                    heapq.heappush(queue, (cost + grid[n_at], n_at, dir2, 1))


with open("input") as file:
    raw = file.read()

lines = raw.strip().split("\n")
grid = make_grid(lines)
goal = max(grid.keys())

p1 = solve(grid, (0, 0), goal, 0, 3)
p2 = solve(grid, (0, 0), goal, 4, 10)

print(p1, p2)
