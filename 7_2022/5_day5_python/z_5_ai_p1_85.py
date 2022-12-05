"""Here is a solution to the problem in Python:

"""
# Read the input file
with open('5_input') as f:
  lines = f.readlines()

# Parse the input
stacks = []
for line in lines:
  stack = []
  for char in line:
    if char.isalpha():
      stack.append(char)
  stacks.append(stack)

# Apply the rearrangement procedure
for line in lines:
  if line.startswith('move'):
    words = line.split()
    n = int(words[1])
    from_stack = int(words[2][:-2])
    to_stack = int(words[5][:-1])
    crate = stacks[from_stack].pop(n)
    stacks[to_stack].append(crate)

# Print the top crates on each stack
for stack in stacks:
  print(stack[-1], end='')
""""""