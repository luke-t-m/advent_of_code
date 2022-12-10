#!/usr/bin/env python3

input = open("10_input").readlines()

x = 1
signal_strengths = []
for instr in input:
    instr = instr.strip().split(" ")
    signal_strengths.append(x)
    if instr[0] == "noop": continue
    elif instr[0] == "addx": 
        signal_strengths.append(x)
        x += int(instr[1])

p1_ans = sum([(c+1) * v for c, v in enumerate(signal_strengths) if c+1 in [20, 60, 100, 140, 180, 220]])
print(f"Part one: {p1_ans}\nPart two:")

for y in range(1, 7):
    print("")
    for x in range(0, 40):
        if abs(x - signal_strengths[40 * (y-1) + x]) <= 1: print("#", end = "")
        else: print(".", end="")
print("\n")
