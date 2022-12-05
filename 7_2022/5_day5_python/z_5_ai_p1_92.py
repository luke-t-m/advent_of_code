"""There are several ways to solve this problem in Python. Here is one possible solution:

"""
# Read input from file "5_input"
with open("5_input") as f:
    lines = f.readlines()

# Parse the input
stacks = []
for line in lines:
    stack = line.strip().split(" ")
    stacks.append(stack)

# Perform the rearrangement steps
for step in steps:
    # Parse the step
    move, quantity, from_stack, _, _, to_stack = step.split(" ")
    quantity = int(quantity)
    from_stack = int(from_stack[1:])
    to_stack = int(to_stack[1:])

    # Move the crates
    crates = stacks[from_stack - 1][-quantity:]
    stacks[from_stack - 1] = stacks[from_stack - 1][:-quantity]
    stacks[to_stack - 1].extend(crates)

# Print the top crates of each stack
for stack in stacks:
    print(stack[-1], end="")
""""""