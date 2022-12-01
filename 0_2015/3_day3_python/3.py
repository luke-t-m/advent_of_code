input = open("input").read()

def solve(input, do_robot=False):
    delivered = set((0, 0))
    x, y, rx, ry = 0, 0, 0, 0
    dxdy = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1,0)}

    for c, v in enumerate(input):
        dx, dy = dxdy[v]
        r = c % 2
        x += (1-(do_robot * r)) * dx
        y += (1-(do_robot * r)) * dy
        rx += do_robot * r * dx
        ry += do_robot * r * dy
        for e in [(x, y), (rx, ry)]: delivered.add(e)
        
    return len(delivered)

print(f"Part one: {solve(input)}")
print(f"Part two: {solve(input, True)}")
