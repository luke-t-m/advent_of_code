#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)


p1 = p2 = 0
inp = sys.argv[1]


output(p1)
output(p2)