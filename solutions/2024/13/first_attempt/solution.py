#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
import numpy as np
import regex as re

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)


p1 = p2 = 0
inp = sys.argv[1]


re_string = "Button A: X\+(\d*), Y\+(\d*)\nButton B: X\+(\d*), Y\+(\d*)\nPrize: X=(\d*), Y=(\d*)"
def solve(pmod):
    out = 0
    for nums in re.findall(re_string, inp):
        ax, ay, bx, by, px, py = map(int, nums)
        px += pmod
        py += pmod
        i = np.array([[ax, bx], [ay, by]])
        j = np.array([px, py])
        s = np.linalg.solve(i, j)
        sa, sb = map(round, s)
        if sa * ax + sb * bx == px and sa * ay + sb * by == py:
            out += sa * 3 + sb
    return out

p1 = solve(0)
p2 = solve(10000000000000)

output(p1)
output(p2)