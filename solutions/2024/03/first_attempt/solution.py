#!/usr/bin/python3
import sys
import re

p1 = p2 = 0
input = sys.argv[1]

lines = input.strip().split("\n")

for l in lines:
    matches = re.findall("mul\((\d*),(\d*)\)", l)
    for m in matches:
        p1 += int(m[0]) * int(m[1])


dos = input.split("do()")
x = []
for d in dos:
    x += d.split("don't()")[:1]
x = "".join(x)

matches = re.findall("mul\((\d*),(\d*)\)", x)
for m in matches:
    p2 += int(m[0]) * int(m[1])


print(p1, p2)