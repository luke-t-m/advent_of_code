"""Here's one way to solve this problem in Python:

"""
# Parse the input
with open("5_input") as f:
    lines = f.read().strip().split("\n")

stacks = []
for line in lines:
    stack = []
    for c in line:
        if c.isalpha():
            stack.append(c)
    stacks.append(stack)

# Perform the rearrangement
for line in lines:
    if line.startswith("move"):
        # Parse the move command
        from_stack, _, _, to_stack = line.split()
        from_stack, to_stack = int(from_stack), int(to_stack)
        # Perform the move
        crate = stacks[from_stack-1].pop()
        stacks[to_stack-1].append(crate)

# Print the final stacks
for stack in stacks:
    print(stack[-1], end="")
print()
""""""