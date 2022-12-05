"""The following code reads the input from the file "5_input" and prints the crates that end up on top of each stack after the rearrangement procedure is completed.

"""
# Read the input from the file "5_input"
with open("5_input") as f:
    input_str = f.read()

# Parse the input string to obtain the starting stacks of crates and the
# rearrangement procedure
lines = input_str.strip().split("\n")

# The first three lines contain the starting stacks of crates
stacks = [list(line) for line in lines[:3]]

# The remaining lines contain the rearrangement procedure
procedure = lines[3:]

# Perform the rearrangement procedure
for step in procedure:
    # Parse the current step
    tokens = step.split()
    num_crates = int(tokens[1])
    from_stack = int(tokens[3])
    to_stack = int(tokens[5])
    
    # Move the specified number of crates from the from_stack to the to_stack
    crates = [stacks[from_stack-1].pop() for _ in range(num_crates)]
    stacks[to_stack-1] = crates + stacks[to_stack-1]

# Print the crates that end up on top of each stack
for stack in stacks:
    print(stack[-1])
""""""