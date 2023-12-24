with open("22/input") as file:
    raw = file.read()

lines = raw.strip().split("\n")

bricks = [[[int(i) for i in j.split(",")] for j in l.split("~")] for l in lines]

blocks = dict()
for i, brick in enumerate(bricks):
    (x1, y1, z1), (x2, y2, z2) = brick
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                blocks[(x, y, z)] = i

done = set()


def drop():
    for i, _ in enumerate(bricks):
        if i in done:
            continue
        oi = [j for j in blocks if blocks[j] == i]
        for (x, y, z) in oi:
            want = (x, y, z - 1)
            if z == 1:
                done.add(i)
            if want in blocks and (i2 := blocks[want]) != i:
                if i2 in done:
                    done.add(i)
                break
        else:
            for b in oi:
                (x, y, z) = b
                blocks.pop(b)
                blocks[(x, y, z-1)] = i


l = len(bricks)
while len(done) != l:
    print(len(done), l)
    drop()
print("-" * (len(str(l)) * 2 + 1), "\n")

supports = dict()

for ind, ((x, y, z), i) in enumerate(blocks.items()):
    if i not in supports:
        supports[i] = set()
    if (x, y, z + 1) in blocks and (oi := blocks[(x, y, z + 1)]) != i:
        supports[i].add(oi)

supported = dict()
for i in supports:
    supported[i] = set()
    for oi in supports:
        if i in supports[oi]:
            supported[i].add(oi)

cant_remove = set()
for i in supported:
    if len(supported[i]) == 1:
        cant_remove.update(supported[i])
p1 = len(supported) - len(cant_remove)

p2 = 0
for i, _ in enumerate(bricks):
    queue = [i]
    unsupported = set(queue)
    while len(queue) != 0:
        at = queue.pop()
        for next in supports[at]:
            if next in unsupported:
                continue
            if supported[next] <= unsupported:
                unsupported.add(next)
                queue.append(next)
    p2 += len(unsupported) - 1

print(p1, p2)
