#!/usr/bin/env python3
import re
from collections import deque

def product(list):
    out = 1
    for i in list: out *= i
    return out

def solve(blueprint, minutes):
    bn, orco, crco, drco, drcc, grco, grcd = blueprint
    queue = deque([(0, 0, 0, 0, 0, 1, 0, 0, 0)])
    visited = set()
    best_g = 0
    while queue:
        state = queue.popleft()
        if state in visited: continue
        visited.add(state)
        m, o, c, d, g, nor, ncr, ndr, ngr = state
        m += 1
        if m > minutes: continue
        if g < best_g - ngr: continue
        best_g = max(g, best_g)
        if len(queue) % 10000 == 0: print(len(queue), m, best_g, bn, end="     \r")
        if o >= grco and d >= grcd: queue.append((m, o-grco+nor, c+ncr, d-grcd+ndr, g+ngr, nor, ncr, ndr, ngr+1))
        if o >= drco and c >= drcc: queue.append((m, o-drco+nor, c-drcc+ncr, d+ndr, g+ngr, nor, ncr, ndr+1, ngr))
        if o >= crco: queue.append((m, o-crco+nor, c+ncr, d+ndr, g+ngr, nor, ncr+1, ndr, ngr))
        if o >= orco and ncr <= 1: queue.append((m, o-orco+nor, c+ncr, d+ndr, g+ngr, nor+1, ncr, ndr, ngr))
        queue.append((m, o+nor, c+ncr, d+ndr, g+ngr, nor, ncr, ndr, ngr))
    print(0, m, best_g, bn, "     ")
    return best_g


input = open("19_input").read()

blueprints = re.findall("Blueprint (\d*): Each ore robot costs (\d*) ore. Each clay robot costs (\d*) ore. Each obsidian robot costs (\d*) ore and (\d*) clay. Each geode robot costs (\d*) ore and (\d*) obsidian.", input)
blueprints = [[int(x) for x in y] for y in blueprints]

print(f"Part one: {sum([b[0] * solve(b, 24) for b in blueprints])}")
print(f"Part two: {product([solve(b, 32) for b in blueprints[:3]])}")