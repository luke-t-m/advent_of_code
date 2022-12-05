"""In order to solve this problem, we need to simulate the rearrangement of the crates according to the given instructions. We can do this by creating a list that represents the stacks of crates, and then using the instructions to move crates from one stack to another.

Here is a possible solution in Python:

"""
# Read the instructions from the input file
with open('5_input', 'r') as f:
  instructions = f.readlines()

# Create a list that represents the stacks of crates
stacks = [['Z'], ['M', 'C', 'D'], ['P']]

# Loop over the instructions
for instruction in instructions:
  # Parse the instruction to get the source and destination stacks
  source, _, dest, _, _ = instruction.split()
  source = int(source) - 1
  dest = int(dest) - 1

  # Move the top crate from the source stack to the destination stack
  top_crate = stacks[source].pop()
  stacks[dest].append(top_crate)

# Print the top crate in each stack
print(''.join([stacks[i][-1] for i in range(len(stacks))]))
""""""