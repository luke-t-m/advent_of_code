import matplotlib.pyplot as plt

with open("18/input") as file:
    raw = file.read()


DIRECTIONS = {"U": (0, -1), "D": (0, 1), "R": (1, 0), "L": (-1, 0)}



def area(points):
    plt.plot(*zip(*points), "-")
    ys = {y for (_, y) in points}
    xs = {x: [] for (x, _) in sorted(points)}
    for (x1, y1), (x2, y2) in zip(points[:-1], points[1:]):
        xs[x1].append(y1)
        for yp in ys:
            if x1 == x2 and y1 < yp < y2:
                xs[x1] += [yp] * 2
    
    for x in xs:
        xs[x].sort()
        plt.plot(*zip(*[(x, y) for y in xs[x]]), "o", color="red")


    area = 0
    print(xs)
    while len(xs) != 0:
        x1, xl = list(xs.items())[0]
        if len(xl) == 0:
            xs.pop(x1)
            continue
        y1 = xl.pop(0)
        y2 = xl.pop(0)
        if y1 == y2:
            continue
        for px, pxl in xs.items():
            print(y1, y2, x1, px)
            if y1 in pxl and y2 in pxl:
                to_add = (px - x1 + 1) * (y2 - y1 + 1)
                plt.plot(*zip((px, y1), (px, y2), (x1, y2), (x1, y1), (px, y1)), "--")
                area += to_add
                print(f"added area: {to_add}, x: {x1}-{px}, y: {y1}-{y2}")
                pxl.remove(y1)
                pxl.remove(y2)
                break
    print(xs)
    print(area)
    plt.gca().invert_yaxis()
    plt.show()

                 
                 
        
            
    
    print(xs)

if 0: raw = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""



lines = raw.strip().split("\n")

at = (0, 0)
points = [at]
for line in lines:
    dir, magn, _ = line.split(" ")
    magn = int(magn)
    at = tuple([(a + b * magn) for (a, b) in zip(at, DIRECTIONS[dir])])
    points.append(at)

p1 = area(points)






