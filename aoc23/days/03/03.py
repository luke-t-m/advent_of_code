with open("input") as file:
    raw = file.read()

lines = raw.strip().split("\n")
mods = [0, -1, 1]
grid = dict()


def get(xy):
    if xy in grid:
        return grid[xy][0]
    return "."


def mark_used(xy):
    if xy in grid:
        grid[xy][1] = True


def is_used(xy):
    if xy in grid:
        return grid[xy][1]


def get_neighbours(x, y):
    out = []
    for mod1 in mods:
        for mod2 in mods:
            if mod1 == 0 and mod2 == 0:
                continue
            out.append(get((x + mod1, y + mod2)))
    return out


def is_partno(neighbours):
    for i in neighbours:
        if not i.isdigit() and i != ".":
            return True
    return False


def gear_ratio(neighbours):
    gears = [int(i) for i in neighbours if i.isdigit()]
    gears = list(set(gears))
    if len(gears) == 2:
        return gears[0] * gears[1]
    return 0


over = [(lines[y][x], (x, y)) for y in range(len(lines)) for x in range(len(lines[0]))]

# parse grid
for at, xy in over:
    if xy[0] == 0:
        cur = ["", False]
    if not at.isdigit():
        grid[xy] = [at, False]
        cur = ["", False]
    else:
        cur[0] += at
        grid[xy] = cur

p1 = p2 = 0
for at, xy in over:
    if at.isdigit() and is_partno(get_neighbours(*xy)) and not is_used(xy):
        p1 += int(get(xy))
        mark_used(xy)
    if at == "*":
        p2 += gear_ratio(get_neighbours(*xy))

print(p1, p2)
