"""The following is a Python program that solves the problem described above. It reads the input from a file called `5_input`, and then it prints the answer.

"""
# Read the input from the file
with open('5_input') as f:
  # Split the input into lines
  lines = f.read().strip().split('\n')

# Parse the input
stacks = []
for line in lines:
  # Split the line into words
  words = line.split()
  # Parse the words
  if words[0] == 'move':
    # This is a move instruction
    # Parse the source and destination stacks
    src_stack = int(words[2])
    dest_stack = int(words[5])
    # Move the top crate from the source stack to the destination stack
    stacks[dest_stack].append(stacks[src_stack].pop())
  else:
    # This is a stack description
    # Parse the crates in the stack
    crates = [crate[1] for crate in words]
    # Add the stack to the list of stacks
    stacks.append(crates)

# Print the top crate in each stack
for i, stack in enumerate(stacks):
  print(f'stack {i}: {stack[-1]}')
""""""