#!/usr/bin/env python3
from itertools import zip_longest
from functools import cmp_to_key

def parse_rec(line, c):
    list = []
    while c <= len(line):
        if line[c] in ", ": pass
        elif line[c] == "[":
            recursed = parse_rec(line, c+1)
            list.append(recursed[0])
            c = recursed[1]
        elif line[c] == "]": return (list, c)
        else:
            to_int = line[c]
            while line[c+1] in "0123456789":
                to_int += line[c+1]
                c += 1
            list.append(int(to_int))
        c += 1

def parse(line):
    line = line.strip()
    return parse_rec(line, 1)[0]

def solve(l, r):
    match l, r:
        case int(), int():
            if l < r: return -1
            elif l > r: return 1
        case int(), list():
            return solve([l], r)
        case list(), int():
            return solve(l, [r])
        case list(), list():
            for el, er in zip_longest(l, r):
                if el == None: return -1
                elif er == None: return 1
                solved = solve(el, er)
                if solved != None: return solved


input = open("13_input").read()

input = input.split("\n\n")
right_order, packets = [], []

for i in input:
    i = i.strip().split("\n")
    l1, l2 = parse(i[0]), parse(i[1])
    packets += [l1, l2]
    if l1 == None or l2 == None: continue
    right_order.append(solve(l1, l2))

print(f"Part one: {sum([c+1 for c, x in enumerate(right_order) if x == -1])}")

packets += [[[2]], [[6]]]

packets.sort(key = cmp_to_key(solve))

p2 = 1
for i in [2, 6]:
    p2 *= packets.index([[i]]) + 1

print(f"Part two: {p2}")
