#!/usr/bin/python3
import sys


def safe(level):
    step = level[1] - level[0]
    if step == 0:
        return False
    else:
        neg = step < 0
    for i in range(0, len(level)-1):
        step = level[i+1] - level[i]
        if (neg and (step >= 0 or step < -3)) or (not neg and (step <= 0 or step > 3)):
            return False
    return True



p1 = p2 = 0
input = sys.argv[1]

lines = input.strip().split("\n")

for l in lines:
    i = list(map(int, l.split()))
    if safe(i):
        p1 += 1
    for n in range(0, len(i)):
        j = list(i)
        j.pop(n)
        if safe(j):
            p2 += 1
            break

print(p1, p2)