#!/usr/bin/python3
import sys

p1 = p2 = 0
input = sys.argv[1]

lines = input.strip().split("\n")

aa = []
bb = []

for l in lines:
    a, b = l.split("   ")
    aa.append(int(a))
    bb.append(int(b))

for a in aa:
    p2 += bb.count(a) * a

while len(aa) != 0:
    smallest_a = min(aa)
    aa.remove(smallest_a)
    smallest_b = min(bb)
    bb.remove(smallest_b)
    p1 += abs(smallest_a - smallest_b)




print(p1, p2)