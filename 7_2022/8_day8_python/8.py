#!/usr/bin/env python3

grid = open("8_input").readlines()

grid = [list(x.strip()) for x in grid]

l, h = len(grid[0]), len(grid)

def direction_check(grid, x, y, p2 = False):
    r, t = int(p2), 0
    for (xl, yl) in [([x]*l, range(y+1, h)),
                     ([x]*l, range(y-1, -1, -1)),
                     (range(x+1, l), [y]*h),
                     (range(x-1, -1, -1), [y]*h)]:
        g = [grid[j][i] for (i, j) in zip(xl, yl)]
        if not p2 and ((x % (l-1)) * (y % (h-1)) == 0 or grid[y][x] > max(g)):
            return 1
        elif p2:
            for k in g:
                t += 1
                if grid[y][x] <= k: break
            r *= t
            t = 0
    return r


no_vis, scenic = 0, 0
for (x, y) in [(x, y) for x in range(l) for y in range(h)]:
    scenic = max(scenic, direction_check(grid, x, y, True))
    no_vis += direction_check(grid, x, y, False)
print(f"Part one: {no_vis}\nPart two: {scenic}")
