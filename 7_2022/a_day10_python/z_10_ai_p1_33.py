"""The following code can be used to solve the problem:

"""
x = 1
signal_strengths = []

with open("10_input") as f:
    for line in f:
        if line.startswith("noop"):
            # noop takes 1 cycle to complete, so we do nothing
            pass
        elif line.startswith("addx"):
            # addx takes 2 cycles to complete
            x += int(line.split()[1])
            signal_strengths.append(x)

# Print the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles
for i in range(20, 220 + 1, 40):
    print(i * signal_strengths[i - 1])
"""

This code reads the instructions from the file `10_input`, simulates the execution of the instructions, and keeps track of the value of the `X` register during each cycle. It then prints the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles as required by the problem statement."""