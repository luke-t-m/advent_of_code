"""The following is a solution to the problem described above in python.

"""
# Parse input
with open("5_input") as f:
  lines = f.readlines()

# Initial configuration of stacks
stacks = []
for i in range(1, len(lines[0]), 4):
  stack = []
  for j in range(3):
    stack.append(lines[j][i])
  stacks.append(stack)

# Rearrangement procedure
for line in lines[3:]:
  words = line.split()
  n = int(words[1])
  from_stack = int(words[3]) - 1
  to_stack = int(words[5]) - 1

  # Remove top n crates from from_stack
  top_crates = stacks[from_stack][-n:]
  stacks[from_stack] = stacks[from_stack][:-n]

  # Add top crates to to_stack
  stacks[to_stack].extend(top_crates)

# Print top crates in each stack
for stack in stacks:
  print(stack[-1])
""""""