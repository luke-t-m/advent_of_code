"""The following code solves the problem correctly in Python.

"""
# Read input from file
f = open("5_input")
input = f.read()
f.close()

# Parse input into list of steps
steps = input.split("\n")
steps = [x for x in steps if x] # Remove empty elements

# Initialize stacks
stacks = [[],[],[]]
stacks[0] = ["Z", "N"]
stacks[1] = ["M", "C", "D"]
stacks[2] = ["P"]

# Perform each step
for step in steps:
    # Parse step into components
    step = step.split(" ")
    n = int(step[1])
    f = int(step[2]) - 1
    t = int(step[5]) - 1

    # Move crates from source stack to target stack
    for i in range(n):
        stacks[t].append(stacks[f].pop())

# Print top crates of each stack
for stack in stacks:
    print(stack[-1], end="")
print()
""""""