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

for p in range(40*6): print(f"\033[1;{31+61*(abs((p%40)-signal_strengths[40*(p//40)+p%40])<=1)}m█\033[0m",end=chr(10*(p%40==39)))
