#!/usr/bin/env python3
import re
import itertools

def do_op(a, op, b):
    match op:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/": return a / b
    assert False

def solve(input, p2=False, guess=0):
    monkes = {}
    for line in itertools.cycle(input):
        r = re.search("(\w{4}): (\d+)", line)
        if r:
            if p2 and r.group(1) == "humn": val = guess
            else: val = int(r.group(2))
            monkes[r.group(1)] = val
            continue
        r = re.search("(\w{4}): (\w{4}) ([+\-*\/]) (\w{4})", line)
        if r and r.group(2) in monkes and r.group(4) in monkes:
            val = do_op(monkes[r.group(2)], r.group(3), monkes[r.group(4)])
            if r.group(1) == "root":
                if p2:
                    a, b = monkes[r.group(2)], monkes[r.group(4)]
                    return (a, b)
                else: return int(val)
            monkes[r.group(1)] = val

def same_sign(a, b):
    return (a > 0) == (b > 0)

def p2(input):
    guess = 0
    guess_mod = 2 ** 40
    dir = 1
    d, pd = None, None
    while True:
        a, b = solve(input, True, guess)
        if a == b:
            print()
            return int(guess)
        pd, d = d, a - b
        if not pd: pd = d
        print(guess, a, b, pd, d, end = "            \r")
        if not same_sign(pd, d):
            dir = -dir
            guess_mod /= 2
        guess += dir * guess_mod


input = open("21_input").readlines()

print(f"Part one: {solve(input)}")
print(f"Part two: {p2(input)}")
