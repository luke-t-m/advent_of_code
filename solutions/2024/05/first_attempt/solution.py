#!/usr/bin/python3
import sys
from itertools import permutations
from queue import Queue

p1 = p2 = 0
inp = sys.argv[1]

inp2 = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

sec1, sec2 = inp.split("\n\n")

lines1 = sec1.strip().split("\n")

lines2 = sec2.strip().split("\n")

rules = []
good = []
for line in lines1:
    a, b = line.split("|")
    rules.append((a, b))

bad = False

p2l = []

def isGood(aa):
    seen = set()
    for a in aa:
        for rule in rules:
            b, c = rule
            if a == b and c in seen:
                return False
        seen.add(a)
    return True


q = Queue()
for line in lines2:
    aa = tuple(line.split(","))
    if isGood(aa):
        p1 += int(aa[int(((len(aa) - 1)/2))])
    else:
        p2l.append(aa)

seen = set()
n = 1


def canAdd(e, l, og):
    if e in l:
        return False
    for (a, b) in rules:
        if e == b:
            if a in og and a not in l:
                return False
    return True

for e, l in enumerate(p2l):
    ll = len(l)
    for i in l:
        q.put([i])
    while q.qsize() != 0:
        used = q.get()
        if len(used) == ll:
            if isGood(used):
                p2 += int(used[int(((len(used) - 1)/2))])
            continue
        for u in l:
            if canAdd(u, used, l):
                new = used + [u]
                q.put(new)



print(p1, p2)