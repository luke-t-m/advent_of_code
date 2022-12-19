#!/usr/bin/env python3
import re
import math
import itertools
from collections import deque
 
def bit_present(bit, bits):
    return (1 << bit) & bits != 0

def time_to_reach(start, stop, neighbours):
    queue = [(start, 0)]
    visited = 0
    while queue:
        pos, time = queue.pop(0)
        if pos == stop: return time
        if bit_present(pos, visited): continue
        visited = visited | (1 << pos)
        for new_pos in neighbours[pos]: queue.append((new_pos, time + 1))
    return math.inf

def make_times_matrix(considered, neighbours):
    times = []
    for valve in considered:
        times.append([])
        for other_valve in considered:
            times[-1].append(time_to_reach(valve, other_valve, neighbours))
    return times

def best_valvage(start, rates, times, n):
    l = len(times)
    # (pos, time, released, on)
    queue = deque([(start, 0, 0, 1 << start)])
    all_on = 2 ** l - 1
    best_released = 0
    while queue:
        pos, time, released, on = queue.popleft()
        if time > n-1: continue
        best_released = max(released, best_released)
        if best_released - released > 300 or on == all_on: continue
        for new_pos in range(l):
            if not bit_present(new_pos, on):
                time_once_on = time + times[pos][new_pos] + 1
                queue.append((new_pos, time_once_on, released + (n-time_once_on) * rates[new_pos], on | (1 << new_pos)))
    return best_released

def make_considered(rates, start, neighbours):
    considered = [i for i, rate in enumerate(rates) if (rate != 0 or i == start)]
    crates = [rate for i, rate in enumerate(rates) if (rate != 0 or i == start)]
    ctimes = make_times_matrix(considered, neighbours)
    cstart = considered.index(start)
    return considered, crates, ctimes, cstart

def with_elephant(considered, rates, cstart, neighbours, n):
    l = len(considered)
    considered.remove(cstart)
    con = list(itertools.combinations(considered, l // 2))
    econ = [[x for x in considered if x not in y] for y in con]
    con = [[start] + list(x) for x in con]
    econ = [[start] + list(x) for x in econ]
    best_released = 0
    lp = len(con)
    for i, (c, ec) in enumerate(zip(con, econ)):
        print(f"{i} / {lp}: {best_released} ", end = "\r")
        rat = [rates[i] for i in c]
        erat = [rates[i] for i in ec]
        tim = make_times_matrix(c, neighbours)
        etim = make_times_matrix(ec, neighbours)
        released = best_valvage(0, rat, tim, n) + best_valvage(0, erat, etim, n)
        best_released = max(released, best_released)
    print(f"{i+1} / {lp}")
    return best_released

input = open("16_input").readlines()

valves, rates, neighbours = [], [], []

for line in input:
    reg = re.search("Valve (..) has flow rate=(\d*); tunnels? leads? to valves? ((?:..,? ?)*)", line)
    if reg:
        valves.append(reg.group(1))
        rates.append(int(reg.group(2)))
        neighbours.append(reg.group(3).split(", "))
neighbours = [[valves.index(a) for a in b] for b in neighbours]
start = valves.index("AA")

considered, crates, ctimes, cstart = make_considered(rates, start, neighbours)

print(f"Part one: {best_valvage(cstart, crates, ctimes, 30)}")
print(f"Part two: {with_elephant(considered, rates, start, neighbours, 26)}")
