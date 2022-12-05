"""The following python code can solve the given problem:

"""
# Read the input from the file
with open("5_input", "r") as input_file:
  input_lines = input_file.readlines()

# Initialize an array of stacks
stacks = []
for i in range(3):
  stacks.append([])

# Parse the initial configuration of stacks
for i, line in enumerate(input_lines[:3]):
  for j, char in enumerate(line):
    if char == "[" or char == "]":
      stacks[j].append(i+1)

# Parse the rearrangement procedure
for line in input_lines[3:]:
  words = line.split()
  # Extract the source and destination stacks
  source = int(words[3])-1
  dest = int(words[-1])-1
  # Extract the number of crates to be moved
  num_crates = int(words[1])
  # Remove the crates from the source stack
  crates = stacks[source][-num_crates:]
  # Remove those crates from the source stack
  stacks[source] = stacks[source][:-num_crates]
  # Add the crates to the destination stack
  stacks[dest] += crates

# Print the top crates of each stack
for stack in stacks:
  print(chr(stack[-1] + ord('A') - 1), end="")
"""

This code first reads the input from the file and initializes an array of stacks. It then parses the initial configuration of stacks and stores them in the array.

Next, it parses the rearrangement procedure and performs the specified moves one by one. Finally, it prints the top crate of each stack, which is the solution to the problem."""