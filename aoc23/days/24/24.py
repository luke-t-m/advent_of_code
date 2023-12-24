import sys

want = "/home/luke/tech/z3/build/python"
if want not in sys.path:
    sys.path.append(want)

import z3


def intersection(hs1, hs2):  # hs2? better hope the tories dont get involved!
    (x1, y1, _), (px1, py1, _) = hs1
    (x3, y3, _), (px3, py3, _) = hs2
    x2, y2 = x1 + px1, y1 + py1
    x4, y4 = x3 + px3, y3 + py3

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    detx = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    dety = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    if denom != 0:
        return detx / denom, dety / denom


def at_time(vars, t):
    x, y, z, px, py, pz = vars
    return x + px * t, y + py * t, z + pz * t


def is_solution(vars1, vars2, t):
    x1, y1, z1 = at_time(vars1, t)
    x2, y2, z2 = at_time(vars2, t)
    return x1 == x2, y1 == y2, z1 == z2


with open("24/input") as file:
    raw = file.read()

lines = raw.strip().split("\n")

hailstones = [[[int(i) for i in j.split(", ")] for j in k.split(" @ ")] for k in lines]
minn = 2 * 10**14
maxx = 4 * 10**14

p1 = sum(
    1
    for ind, hs1 in enumerate(hailstones)
    for hs2 in hailstones[ind + 1 :]
    if (intersect := intersection(hs1, hs2)) is not None
    and all(minn <= i <= maxx for i in intersect)
    and all(0 <= (intersect[0] - hs[0][0]) / hs[1][0] for hs in [hs1, hs2])
)

vars = dict()
for var in ["x", "y", "z", "px", "py", "pz"]:
    vars[var] = z3.Int(var)

solver = z3.Solver()

for i, hs in enumerate(hailstones[:3]):
    for sol in is_solution(vars.values(), [v for p in hs for v in p], z3.Int(str(i) + "ns")):
        solver.add(sol)

print(f"check: {solver.check()}\n{'-' * 10}\n")
m = solver.model()

p2 = sum(int(str(m[vars[var]])) for var in ["x", "y", "z"])

print(p1, p2)
