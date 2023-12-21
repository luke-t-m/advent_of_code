from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def make_grid(ls):
    return {(x, y): c for y, r in enumerate(ls) for x, c in enumerate(r)}


def solve_p2(lines):
    grid = make_grid(lines)
    want = 26501365
    os = set()
    w = len(lines)
    lo1 = lo2 = lo3 = 0
    queue = deque([(start, 0)])
    seen = set()
    while True:
        new_q = deque()
        while len(queue) != 0:
            state = queue.pop()
            at, i = state
            real_at = (at[0] % w, at[1] % w)
            if at in seen or grid[real_at] not in ".S":
                continue
            seen.add(at)

            for dir in DIRECTIONS:
                n_at = tuple(a + b for (a, b) in zip(at, dir))
                new_q.append((n_at, i + 1))

            if i % 2 == 1:
                os.add(at)
        queue = new_q

        if i % (2 * w) == want % (2 * w):
            o1 = len(os)
            o2 = o1 - lo1
            o3 = o2 - lo2
            if o3 == lo3:
                n = (want - i) // (2 * w)
                return o1 + n * o2 + n * (n + 1) // 2 * o3
            lo1, lo2, lo3 = o1, o2, o3


with open("21/input") as file:
    raw = file.read()

lines = raw.strip().split("\n")

grid = make_grid(lines)
for i in grid:
    if grid[i] == "S":
        start = i
        break


queue = deque([(start, 0)])
seen = set()
reachable = set()
while len(queue) != 0:
    state = queue.pop()
    at, steps = state
    if state in seen or at not in grid or grid[at] not in ".S":
        continue
    seen.add(state)

    if steps == 64:
        reachable.add(at)
    else:
        for dir in DIRECTIONS:
            n_at = tuple(i + j for (i, j) in zip(at, dir))
            queue.append((n_at, steps + 1))


p1 = len(reachable)
p2 = solve_p2(lines)

print(p1, p2)
