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


#input = "do()xdon't()ydo()xdon't()ydon't()y"

dos = input.split("do()")
x = []
for d in dos:
    x += d.split("don't()")[:1]
x = "".join(x)

dos = input.split("don't()")
y = [dos[0]]
for d in dos[1:]:
    y += d.split("do()")[1:]
y = "".join(y)


matches = re.findall("mul\((\d*),(\d*)\)", x)
matches2 = re.findall("mul\((\d*),(\d*)\)", y)

for m, m2 in zip(matches, matches2):
    p2 += int(m[0]) * int(m[1])

 
print(p1, p2)