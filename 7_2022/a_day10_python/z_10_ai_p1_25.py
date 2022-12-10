"""The code to solve the problem is as follows:

"""
# Open the input file
with open('10_input', 'r') as f:
  # Read the instructions from the file
  instructions = f.readlines()

# Initialize the X register to 1
X = 1

# Iterate over the instructions
for i, instruction in enumerate(instructions):
  # Split the instruction into its parts
  parts = instruction.split()

  # If the instruction is "noop", do nothing
  if parts[0] == "noop":
    continue

  # If the instruction is "addx", add the value to the X register
  elif parts[0] == "addx":
    X += int(parts[1])

# Print the final value of X
print(X)
""""""