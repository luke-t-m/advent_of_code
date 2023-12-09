with open("input") as file:
    raw = file.read()

lines = raw.strip().split("\n")

instr = lines[0]
nodes = dict()


for line in lines[2:]:
    x, lr = line[:-1].split(" = (")
    l, r = lr.split(", ")
    nodes[x] = (l, r)


no_ends = len([n for n in nodes if n[-1] == "Z"])


def find_loop(start):
    at = start
    first_seen = None
    ind = 0
    while True:
        i = instr[ind % len(instr)]
        ind += 1
        if at[-1] == "Z":
            if first_seen is None:
                first_seen = ind
            else:
                return ind - first_seen
        if i == "L":
            at = nodes[at][0]
        elif i == "R":
            at = nodes[at][1]


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return abs(x)


p1 = 0
ind = 0
at = "AAA"
while True:
    i = instr[ind % len(instr)]
    ind += 1
    if at == "ZZZ":
        break
    if i == "L":
        at = nodes[at][0]
    elif i == "R":
        at = nodes[at][1]
    p1 += 1

loops = [find_loop(i) for i in nodes if i[-1] == "A"]

p2 = 1
for i in loops:
    p2 = p2 * i // gcd(p2, i)

print(p1, p2)
