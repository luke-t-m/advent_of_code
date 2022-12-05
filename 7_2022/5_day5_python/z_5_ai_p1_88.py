"""Here is the solution in Python:

"""
# Read input from 5_input file
with open("5_input") as f:
    data = f.read().strip().split("\n")

# Parse input data
stacks = [[c for c in line.strip()] for line in data[:-1]]
steps = [line.strip() for line in data[-1:][0].split("\n")]

# Function to move topmost crate from one stack to another
def move(stacks, from_stack, to_stack):
    # Get the top crate
    top_crate = stacks[from_stack].pop()
    # Add it to the top of the destination stack
    stacks[to_stack].append(top_crate)

# Function to move multiple crates from one stack to another
def move_multiple(stacks, from_stack, to_stack, num_crates):
    for _ in range(num_crates):
        # Move one crate at a time
        move(stacks, from_stack, to_stack)

# Perform the steps given in the input
for step in steps:
    # Parse step
    words = step.split()
    num_crates = int(words[1])
    from_stack = int(words[2]) - 1
    to_stack = int(words[5]) - 1
    # Perform the move
    move_multiple(stacks, from_stack, to_stack, num_crates)

# Print the top crate of each stack
for i, stack in enumerate(stacks):
    print(f"Stack {i+1}: {stack[-1]}")
"""

The solution can be tested using the input provided in the problem statement. The top crate of each stack should be printed at the end:

"""
Stack 1: C
Stack 2: M
Stack 3: Z
""""""