from operator import gt, lt
from functools import reduce


def make_entry(p, op, num, goto, goto2, is_p2):
    return (
        (p, op, num, goto, goto2) if is_p2
        else lambda part: goto if op(part[p], num) else goto2
    )


def make_entry2(goto, is_p2):
    return goto if is_p2 else lambda _: goto


def make_rules(workflows, is_p2=False):
    rules = dict()
    for workflow in workflows:
        name, bits = workflow.split("{")
        bits = bits[:-1].split(",")
        for a in bits[:-1]:
            rules[name] = make_entry(
                a[0],
                lt if a[1] == "<" else gt,
                int(a.split(":")[0][2:]),
                a.split(":")[1],
                name + "+",
                is_p2,
            )
            name += "+"
        rules[name] = make_entry2(bits[-1], is_p2)
    return rules


def solve2(rules, ranges, at, update=None):
    ranges = {i: ranges[i] for i in ranges}
    if update is not None:
        ranges.update(update)

    if at == "A":
        return reduce(lambda a, r: a * (r[1] - r[0] + 1), ranges.values(), 1)
    if at == "R":
        return 0

    rule = rules[at]
    if isinstance(rule, str):
        return solve2(rules, ranges, rule)

    p, op, num, goto, goto2 = rule

    l, h = ranges[p]
    if op is gt:
        good = (max(num + 1, l), h)
        bad = (l, min(num, h))
    else:
        good = (l, min(num - 1, h))
        bad = (max(num, l), h)

    return (solve2(rules, ranges, goto, {p: good}) + 
            solve2(rules, ranges, goto2, {p: bad}))


with open("input") as file:
    raw = file.read()

ws, ps = [i.split("\n") for i in raw.strip().split("\n\n")]

parts = [{(b := a.split("="))[0]: int(b[1]) for a in p[1:-1].split(",")} for p in ps]
rules = make_rules(ws)

p1 = 0
for part in parts:
    at = "in"
    while at not in ["A", "R"]:
        at = rules[at](part)
    if at == "A":
        p1 += sum(part.values())

rules = make_rules(ws, is_p2=True)
p2 = solve2(rules, {p: (1, 4000) for p in ["x", "m", "a", "s"]}, "in")

print(p1, p2)
