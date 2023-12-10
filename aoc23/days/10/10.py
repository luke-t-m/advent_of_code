with open("input") as file:
    raw = file.read()


lines = raw.strip().split("\n")
p1 = p2 = 0


grid = dict()
for y, line in enumerate(lines):
    for x, el in enumerate(line):
        grid[(x, y)] = el
        if el == "S":
            start = (x, y)


pipes = {
    "|": (0, 2),
    "-": (1, 3),
    "L": (0, 1),
    "J": (0, 3),
    "7": (2, 3),
    "F": (1, 2),
}

directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

outline = []
for pos_start_pipe in pipes:
    grid[start] = pos_start_pipe
    at = start
    seen = set()
    direction = pipes[pos_start_pipe][0]
    while at not in seen and at in grid:
        seen.add(at)
        type = grid[at]
        if type not in pipes:
            break
        direction = [i for i in pipes[type] if i != (direction + 2) % 4][0]
        xmod, ymod = directions[direction]
        at = at[0] + xmod, at[1] + ymod

    else:
        if len(seen) > len(outline):
            outline = seen
    grid[start] = "S"

p1 = len(outline) // 2


seen = set()
for y in range(len(lines)):
    is_inside = False
    opener = None
    for x in range(len(lines[y])):
        at = (x, y)
        what = grid[at]
        if at in outline:
            if (
                what == "|"
                or what == "J"
                and opener == "F"
                or what == "7"
                and opener == "L"
            ):
                is_inside = not is_inside
                opener = None
            elif what in "LF":
                opener = what
        elif is_inside:
            seen.add(at)
p2 = len(seen)

print(p1, p2)
