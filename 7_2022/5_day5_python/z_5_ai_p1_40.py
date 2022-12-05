"""To solve this problem, you can use a simple simulation. You can create a list of lists that represents the stacks of crates and then iterate through the rearrangement instructions, moving the crates as needed.

Here is an example of how you can solve this problem in Python:

"""
# Read the input from the file
with open('5_input') as f:
  instructions = f.read().strip().split('\n')

# Create a list of lists that represents the stacks of crates
stacks = [['Z'], ['M', 'C', 'D'], ['P']]

# Iterate through the instructions
for instruction in instructions:
  # Parse the instruction
  from_stack, _, to_stack, _, _ = instruction.split()

  # Move the top crate from the "from" stack to the "to" stack
  stacks[int(to_stack)-1].append(stacks[int(from_stack)-1].pop())

# Print the top crate in each stack
for stack in stacks:
  print(stack[-1], end='')
"""

This code will read the input from the file `5_input`, create a list of lists that represents the stacks of crates, and then simulate the rearrangement procedure. After the procedure is complete, it will print the top crate in each stack."""