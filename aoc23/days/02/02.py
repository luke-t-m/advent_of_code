with open("input") as file:
    raw = file.read()
lines = raw.strip().split("\n")


def getMinBalls(subsets):
    out = {"red": 0, "green": 0, "blue": 0}
    for subset in subsets:
        balls = subset.split(",")
        for ball in balls:
            no = int("".join(c for c in ball if c.isdigit()))
            colour = "".join(c for c in ball if c.isalpha())
            out[colour] = max(out[colour], no)
    return out


amounts = {"red": 12, "green": 13, "blue": 14}

p1 = 0
p2 = 0
for order_no, line in enumerate(lines, 1):
    line = line.split(":")[1]
    subsets = line.split(";")
    min_balls = getMinBalls(subsets)

    for colour in amounts:
        if min_balls[colour] > amounts[colour]:
            break
    else:
        p1 += order_no
    p2 += min_balls["red"] * min_balls["green"] * min_balls["blue"]

print(p1, p2)
