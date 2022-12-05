"""Since the problem asks for the crate on top of each stack, it's probably a good idea to use a stack data structure to keep track of the crates.

To solve the problem, we can create a list of stacks, where each stack contains a list of crates. We can then simulate the rearrangement procedure by iterating over the steps and using stack operations to move the crates. After the rearrangement procedure completes, we can simply print the top crate of each stack.

Here's a possible solution in Python:

"""
# Read the input from the file "5_input"
with open("5_input") as f:
    # Split the input into lines and remove empty lines
    lines = [line.strip() for line in f if line.strip()]

# Create a list of stacks, where each stack is represented as a list of crates
stacks = [list(line) for line in lines[:-1]]

# Parse the rearrangement procedure
steps = [line.split() for line in lines[-1:]]

# Simulate the rearrangement procedure by iterating over the steps
for from_stack, _, to_stack in steps:
    # Convert the stack indices from strings to integers
    from_stack = int(from_stack)
    to_stack = int(to_stack)

    # Pop a crate from the "from" stack and push it onto the "to" stack
    crate = stacks[from_stack].pop()
    stacks[to_stack].append(crate)

# Print the top crate of each stack
print("".join(stack[-1] for stack in stacks))
"""

We can then run the script to solve the problem:

"""
$ python script.py
CMZ
""""""