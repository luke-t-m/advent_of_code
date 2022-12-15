#!/usr/bin/env python3
import re

file = open("4_input")
lines = file.readlines()
file.close()

lines = map(lambda x: re.split("-|,", x[:-1]), lines)
lines = list(map(lambda x: list(map(int, x)), lines))



print(f"Part one: {len([a for a, b, c, d in lines if (a >= c and b <= d) or (c >= a and d <= b)])}")
print(f"Part two: {len([a for a, b, c, d in lines if (b >= c and a <= d) or (a >= d and b <= c)])}")
