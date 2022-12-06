#!/usr/bin/env python3
import re

file = open("4_input")
lines = file.readlines()
file.close()

lines = map(lambda x: re.split("-|,", x[:-1]), lines)
lines = map(lambda x: list(map(int, x)), lines)

p1 = [x for x in lines if (x[0] >= x[2] and x[1] <= x[3]) or (x[2] >= x[0] and x[3] <= x[1])] # whyt this breaking?????
p2 = [x for x in lines if (x[1] >= x[2] and x[0] <= x[3]) or (x[0] >= x[3] and x[1] <= x[2])]
print(p2)
#print(f"Part one: {len(p1)}")
print(f"Part two: {len(p2)}")
