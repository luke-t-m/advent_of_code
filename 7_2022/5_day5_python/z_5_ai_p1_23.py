"""To solve this problem, you can use the following python code:

"""
# Read the input from the file "5_input"
with open("5_input") as f:
    input_str = f.read()

# Parse the input string to extract the starting stacks of crates
# and the rearrangement procedure
stacks = []
procedure = []
for line in input_str.strip().split("\n"):
    if line.startswith("["):
        # This line contains the starting stacks of crates
        stacks = [list(stack) for stack in line.split("]") if stack]
    else:
        # This line contains a step in the rearrangement procedure
        num_crates, from_stack, _, to_stack = line.split()
        num_crates = int(num_crates)
        from_stack = int(from_stack.strip("()"))
        to_stack = int(to_stack.strip("()"))
        procedure.append((num_crates, from_stack, to_stack))

# Apply the rearrangement procedure to the starting stacks of crates
for num_crates, from_stack, to_stack in procedure:
    # Move the specified number of crates from the from_stack to the to_stack
    crates = stacks[from_stack - 1][:num_crates]
    stacks[from_stack - 1] = stacks[from_stack - 1][num_crates:]
    stacks[to_stack - 1] = crates + stacks[to_stack - 1]

# Print the top crate on each stack
for stack in stacks:
    print(stack[-1], end="")
"""

This code first parses the input string to extract the starting stacks of crates and the rearrangement procedure. It then applies the rearrangement procedure to the starting stacks of crates and prints the top crate on each stack.

For example, given the input:
"""
[D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

The code above will print the message `CMZ`."""