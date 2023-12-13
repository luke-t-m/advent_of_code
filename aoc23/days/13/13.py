with open("input") as file:
    raw = file.read()


def transpose(grid):
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]


def find_mirror(grid):
    for y in range(1, len(grid) // 2 + 1):
        up_to = grid[:y]
        #print(up_to + up_to[::-1], grid[:y*2+1])
        if up_to + up_to[::-1] == grid[:y*2]:
            return y
    return 10000000


def solve(grid):
    out = []
    out.append(100 * find_mirror(grid))
    out.append(100 * (len(grid) - find_mirror(grid[::-1])))
    grid = transpose(grid)
    out.append(find_mirror(grid))
    out.append(len(grid) - find_mirror(grid[::-1]))
    return [i for i in out if abs(i) <= 1000000]

def flip(i):
    if i == ".": return "#"
    if i == "#": return "."

def do_p2(grid):
    out = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = flip(grid[y][x])
            o = solve(grid)
            if o is not None:
                out += o
            grid[y][x] = flip(grid[y][x])
    return min(out, key=out.count)



p1 = p2 = 0
patterns = raw.strip().split("\n\n")
for pattern in patterns:
    grid = [list(i) for i in pattern.split("\n")]
    p1 += solve(grid)[0]
    p2 += do_p2(grid)

print(p1, p2)

