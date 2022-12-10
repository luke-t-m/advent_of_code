"""The following is a solution to the problem in Python:

"""
# Parse the input
instructions = []
with open("10_input") as f:
    for line in f:
        if line.startswith("addx"):
            instructions.append((int(line[5:]), 2))
        elif line.startswith("noop"):
            instructions.append((0, 1))

# Execute the instructions
X = 1
signal_strength = 0
for cycle in range(1, 300):
    # Check if this is a cycle we should be looking at
    if cycle % 40 == 20:
        signal_strength += cycle * X
    # Execute the next instruction
    instr, cycles = instructions[(cycle - 1) % len(instructions)]
    if cycles > 1:
        instructions[(cycle - 1) % len(instructions)] = (instr, cycles - 1)
    else:
        X += instr

# Print the answer
print(signal_strength)
"""

This solution first parses the input file and stores the instructions in a list. It then executes the instructions, keeping track of the value of the X register and the signal strength. Finally, it prints the answer (the total signal strength)."""