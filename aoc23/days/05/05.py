with open("input") as file:
    raw = file.read()

lines = raw.strip().split("\n")

seeds = [int(x) for x in lines[0].split(":")[1].split(" ") if x.isdigit()]


maps = []
smaps = raw.split("\n\n")[1:]

for map in smaps:
    lines = map.split("\n")
    name = lines[0][:-5]
    n1, n2 = name.split("-to-")
    rules = []
    for rule in lines[1:]:
        rule = [int(x) for x in rule.split(" ") if x.isdigit()]
        if len(rule) == 3:
            rules.append(rule)
    maps.append((n1, n2, rules))


def apply_rule(cur, what):
    for n1, n2, rules in maps:
        if n1 != what:
            continue
        for ds, ss, l in rules:
            if cur >= ss and cur < ss + l:
                return ds + (cur - ss), n2
        return cur, n2


p1 = 99999999999999999999999999999

for x, seed in enumerate(seeds):
    cur = seed
    what = "seed"
    while what != "location":
        cur, what = apply_rule(cur, what)
    p1 = min(cur, p1)


def apply_rule_rev(cur, what):
    for n1, n2, rules in maps:
        if n2 != what:
            continue
        for ds, ss, l in rules:
            if cur >= ds and cur < ds + l:
                return ss + (cur - ds), n1
        return cur, n1


ranges = []
for x in range(0, len(seeds), 2):
    ranges.append(seeds[x : x + 2])


def in_ranges(n):
    for s, l in ranges:
        if s <= n <= s + l:
            return True
    return False


def do_reversing(s, e, step):
    for pos in range(s, e, step):
        cur = pos
        what = "location"
        while what != "seed":
            cur, what = apply_rule_rev(cur, what)
        if in_ranges(cur):
            return pos


step = 100000
found = do_reversing(0, 99999999999999999, step)
actual = do_reversing(found - step, found, 1)

print(p1, actual)
