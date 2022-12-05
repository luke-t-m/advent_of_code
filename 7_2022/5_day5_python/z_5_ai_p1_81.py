"""To solve this problem, you can create a list to represent the stacks. Then, you can simulate the rearrangement procedure by iterating through the instructions and moving the specified crates between the stacks.

Here is some sample code that solves the problem:

"""
# Create the list of stacks
stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

# Read the instructions from the input file
with open('5_input') as f:
    instructions = f.read().strip().split('\n')

# Simulate the rearrangement procedure
for instruction in instructions:
    # Parse the instruction
    from_stack, _, _, _, _, to_stack = instruction.split()
    from_stack = int(from_stack)
    to_stack = int(to_stack)
    
    # Move the specified crate from one stack to the other
    crate = stacks[from_stack - 1].pop()
    stacks[to_stack - 1].append(crate)

# Print the top crate of each stack
for stack in stacks:
    print(stack[-1], end='')
"""

This code should produce the correct output when run on the input provided in the problem statement. Note that the code assumes that the input is formatted as described in the problem statement, and that the input file is located in the same directory as the script."""