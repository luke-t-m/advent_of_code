"""Here is a correct implementation of the puzzle in Python:

"""
# Read the input from the file "5_input"
with open('5_input') as f:
  lines = f.readlines()

# Parse the input
num_stacks = int(lines[0])
stacks = [[int(x) for x in line.strip().split()] for line in lines[1:num_stacks+1]]
moves = [[int(x) for x in line.strip().split()] for line in lines[num_stacks+1:]]

# Simulate the moves
for move in moves:
  # Remove the crates from the source stack
  crates = stacks[move[1]][move[0]:]

  # Remove the crates from the source stack
  stacks[move[1]] = stacks[move[1]][:move[0]]

  # Add the crates to the destination stack
  stacks[move[2]] += crates

# Print the top crate of each stack
for stack in stacks:
  print(stack[-1])
""""""