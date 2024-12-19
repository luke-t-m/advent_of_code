#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
from collections import deque

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)

inp = sys.argv[1].strip()

parts, wants = inp.split("\n\n")
parts = parts.split(", ")
wants = wants.split("\n")

def can_make(want, parts):
    dq = deque([0])
    seen = set()
    lwant = len(want)
    while dq:
        at = dq.pop()
        for part in parts:
            lpart = len(part)
            nat = at + lpart
            if nat <= lwant and nat not in seen and part == want[at:nat]:
                if nat == lwant:
                    return True
                seen.add(nat)
                dq.append(nat)
    return False

seen = {"": 1}
def can_make_rec(want):
    if want in seen:
        return seen[want]
    out = 0
    for p in parts:
        lp = len(p)
        if want[-lp:] == p:
            out += can_make_rec(want[:-lp])
    seen[want] = out
    return out


p1 = len([i for i in wants if can_make(i, parts)])
p2 = sum([can_make_rec(i) for i in wants])

output(p1)
output(p2)