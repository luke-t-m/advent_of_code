with open("input") as file:
    raw = file.read()

lines = raw.strip().split("\n")
p1 = p2 = 0

mem = dict()

def solve(parts, secs, l=0):
    if (state := (parts, secs, l)) in mem:
        return mem[state]
    elif len(secs) == 0:
        return int("#" not in parts)
    elif len(parts) == 0:
        return int(len(secs) == 0)
    out = 0
    p = parts[0]
    if p in "#?":
        out += solve(parts[1:], secs, l+1)
    if p in ".?":
        if l == 0:
            out += solve(parts[1:], secs)
        elif l == secs[0]:
            out += solve(parts[1:], secs[1:])
    mem[state] = out
    return out


def parse_solve(line, mult=1):
    parts, secs = line.split(" ")
    parts = "?".join(parts for _ in range(mult))
    secs = ",".join(secs for _ in range(mult))

    parts = "." + parts + "."
    secs = tuple([int(s) for s in secs.split(",")])
    return solve(parts, secs)


p1 = sum([parse_solve(line) for line in lines])
p2 = sum([parse_solve(line, 5) for line in lines])

print(p1, p2)
