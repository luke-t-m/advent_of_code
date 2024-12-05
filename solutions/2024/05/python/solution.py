#!/usr/bin/python3
import sys
from queue import Queue


def lines(raw):
    return raw.strip().split("\n")

def isGood(aa):
    seen = set()
    for a in aa:
        for rule in rules:
            b, c = rule
            if a == b and c in seen:
                return False
        seen.add(a)
    return True

def getMid(l):
    return int(l[int(((len(l) - 1)/2))])

def canAdd(e, l, og):
    if e in l:
        return False
    for (a, b) in rules:
        if ((e == b and a in og and a not in l) or
            (e == a and b in l)):
            return False
    return True


p1 = p2 = 0
inp = sys.argv[1]

sec1, sec2 = inp.split("\n\n")
rules = [line.split("|") for line in lines(sec1)]
p2l = []


q = Queue()
for line in lines(sec2):
    pages = line.split(",")
    if isGood(pages):
        p1 += getMid(pages)
    else:
        p2l.append(set(pages))


for l in p2l:
    q.put([])
    while True:
        w = q.get()
        if len(w) == len(l):
            p2 += getMid(w)
            break
        for u in l:
            if canAdd(u, w, l):
                new = w + [u]
                q.put(new)



print(p1, p2)