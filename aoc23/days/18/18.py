DIRS = {"U": (0, -1), "D": (0, 1), "R": (1, 0), "L": (-1, 0)}
DIRS2 = {"3": (0, -1), "1": (0, 1), "0": (1, 0), "2": (-1, 0)}


def shoelace(points):
    pairs = zip(points, [*points[1:], points[0]])
    return sum([x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in pairs]) // 2


def rev_picks(a, b):
    return a + b // 2 + 1


def solve(moves):
    at, b = (0, 0), 0
    points = [at]
    for dir, magn in moves:
        at = tuple([(i + m * magn) for (i, m) in zip(at, dir)])
        points.append(at)
        b += magn

    print(rev_picks(shoelace(points), b))


with open("18/input") as file:
    lines = file.read().strip().split("\n")

solve((DIRS[(s := l.split(" "))[0]], int(s[1])) for l in lines)
solve((DIRS2[(h := l.split(" ")[2])[-2]], int(h[2:][:-2], 16)) for l in lines)
