"""Here is a possible solution to the problem in python:

"""
# Read the input
with open("5_input") as f:
  instructions = f.read().strip().split("\n")

# Initialize the stacks
stacks = [[], [], []]

# Initialize the top crates
top_crates = ["", "", ""]

# Parse the instructions
for instruction in instructions:
  # Parse the instruction
  from_stack, _, _, _, _, _, to_stack = instruction.split()
  from_stack = int(from_stack)
  to_stack = int(to_stack)

  # Move the crates
  stacks[to_stack - 1].append(stacks[from_stack - 1].pop())

  # Update the top crates
  for i in range(3):
    if stacks[i]:
      top_crates[i] = stacks[i][-1]

# Print the result
print("".join(top_crates))
""""""