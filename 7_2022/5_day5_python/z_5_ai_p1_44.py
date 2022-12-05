"""The problem requires us to simulate a series of crate movements. We can do this by storing the current state of the stacks in a list of lists, where each inner list represents a stack and contains the crates in that stack from top to bottom.

We can then implement the crate movement instructions by popping a crate from the source stack and appending it to the destination stack.

Here is a solution in Python:

"""
# Read the input
with open("5_input") as f:
    lines = [line.strip() for line in f.readlines()]

# Parse the input to get the starting stack configuration and the instructions
stacks = [[crate for crate in stack] for stack in lines[0].split(" ")]
instructions = [line.split(" ") for line in lines[1:]]

# Simulate the crate movement instructions
for instruction in instructions:
    # Parse the instruction
    src, _, dest, _, _ = instruction

    # Get the source and destination stack indices
    src_idx = int(src[1]) - 1
    dest_idx = int(dest[1]) - 1

    # Pop the top crate from the source stack and append it to the destination stack
    crate = stacks[src_idx].pop()
    stacks[dest_idx].append(crate)

# Print the final stack configuration
print("".join(stacks[0]))
print("".join(stacks[1]))
print("".join(stacks[2]))
"""

Running this code on the example input in the problem statement should produce the output `CMZ`."""