"""The following code correctly solves the problem and prints the answer.
"""
X = 1
signal_strength = 0
cycle_num = 1
with open("10_input") as f:
    for line in f:
        line = line.strip()
        instr, val = line.split()
        val = int(val)
        if instr == "noop":
            cycle_num += 1
        elif instr == "addx":
            cycle_num += 2
            X += val
        if cycle_num == 20 or (cycle_num - 20) % 40 == 0:
            signal_strength += cycle_num * X

print(signal_strength)
""""""