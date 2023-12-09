from functools import reduce


def parse1(line):
    return [int(i) for i in line.split() if i.isdigit()]


def parse2(line):
    return [int("".join([i for i in line.split() if i.isdigit()]))]


def solve(times, dists):
    return [
        sum([1 for i in range(1, time) if i * (time - i) > dist])
        for time, dist in zip(times, dists)
    ]


with open("input") as file:
    raw = file.read()

times, dists = raw.strip().split("\n")

p1 = reduce(lambda i, j: i * j, solve(parse1(times), parse1(dists)))

p2 = solve(parse2(times), parse2(dists))[0]

print(p1, p2)
