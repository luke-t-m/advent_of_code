"""The following code solves the problem as described above.

"""
# read input
with open('10_input', 'r') as f:
    instructions = f.read().strip().split('\n')

# initialize X
X = 1

# iterate through instructions
for i, instr in enumerate(instructions):
    # if the instruction is "noop", do nothing
    if instr == "noop":
        continue

    # if the instruction is "addx V", increase X by V after two cycles
    if instr.startswith("addx"):
        V = int(instr.split()[1])
        if (i + 2) % 40 == 19:
            X += V

# print the result
print(X)
""""""