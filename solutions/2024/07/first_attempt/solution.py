#!/usr/bin/python3
import sys
from itertools import product

p1 = p2 = 0
inp = sys.argv[1]


lines = inp.strip().split("\n")

mult = lambda a, b: a*b
add = lambda a, b: a+b
concat = lambda a, b: int(f"{a}{b}")


def solve(ops):
    out = 0
    oppps = dict()

    for l in lines:
        want, nums = l.split(":")
        want = int(want)
        nums = nums.split()
        nums = list(map(int, nums))
        ln = len(nums)
        if ln not in oppps:
            opps = list(product(ops, repeat=len(nums) - 1))
            oppps[ln] = opps
        else:
            opps = oppps[ln]
        for p in opps:
            wrk = nums[0]
            for i, n in enumerate(nums[1:]):
                op = p[i]
                wrk = op(wrk, n)
            if wrk == want:
                out += want
                break
    return out

p1 = solve([add, mult])
p2 = solve([add, mult, concat])
    

print(p1, p2)