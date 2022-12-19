#!/usr/bin/env python3
import re
from collections import deque
from multiprocessing import Pool
from itertools import repeat
from os import cpu_count
import time



def product(list):
    out = 1
    for i in list: out *= i
    return out

def solve(blueprint, minutes, p2 = False):
    start_time = time.time()
    bn, orco, crco, drco, drcc, grco, grcd = blueprint
    print(f"STARTING {bn}")
    queue = deque([(0, 0, 0, 0, 0, 1, 0, 0, 0)])
    visited = set()
    best_g = 0
    while queue:
        state = queue.popleft()
        if state in visited: continue
        visited.add(state)
        m, o, c, d, g, nor, ncr, ndr, ngr = state
        if g < best_g - ngr: continue
        best_g = max(g, best_g)
        m += 1
        if m > minutes: continue
        if o >= grco and d >= grcd: queue.append((m, o-grco+nor, c+ncr, d-grcd+ndr, g+ngr, nor, ncr, ndr, ngr+1))
        if o >= drco and c >= drcc: queue.append((m, o-drco+nor, c-drcc+ncr, d+ndr, g+ngr, nor, ncr, ndr+1, ngr))
        if o >= crco: queue.append((m, o-crco+nor, c+ncr, d+ndr, g+ngr, nor, ncr+1, ndr, ngr))
        if o >= orco and ncr <= 1: queue.append((m, o-orco+nor, c+ncr, d+ndr, g+ngr, nor+1, ncr, ndr, ngr))
        queue.append((m, o+nor, c+ncr, d+ndr, g+ngr, nor, ncr, ndr, ngr))
    delta = time.time() - start_time
    print(f"RESULT {bn} = {best_g} in {round(delta, 3)}")
    if p2: return best_g
    return best_g * bn
 

input = open("19_input").read()

blueprints = re.findall("Blueprint (\d*): Each ore robot costs (\d*) ore. Each clay robot costs (\d*) ore. Each obsidian robot costs (\d*) ore and (\d*) clay. Each geode robot costs (\d*) ore and (\d*) obsidian.", input)
blueprints = [[int(x) for x in y] for y in blueprints]

new = [0, 2, 5, 0, 0, 2, 1, 0, 0, 5, 0, 0, 10, 6, 0, 2, 11, 1, 0, 9, 0, 4, 0, 2, 0, 1, 0, 0, 0, 9]
old = [0, 4, 15, 0, 0, 12, 7, 0, 0, 50, 0, 0, 130, 84, 0, 32, 187, 18, 0, 180, 0, 88, 0, 48, 0, 26, 0, 0, 0, 270]


pool = Pool(cpu_count())
print(f"Part one: {sum(pool.starmap(solve, zip(blueprints, repeat(24))))}")
print(f"Part two: {product(pool.starmap(solve, zip(blueprints[:3], repeat(32), repeat(True))))}")