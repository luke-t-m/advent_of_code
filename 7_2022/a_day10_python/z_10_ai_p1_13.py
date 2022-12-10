"""The following code can be used to solve the problem:

"""
# Read the input from the file
with open("10_input", "r") as f:
  instructions = f.read().split("\n")

# Initialize the X register
x = 1

# Keep track of the signal strength
signal = 0

# Loop through the instructions
for i, instruction in enumerate(instructions):
  if instruction == "noop":
    # No operation
    pass
  elif instruction.startswith("addx"):
    # Parse the value to add to the X register
    value = int(instruction.split(" ")[1])
    x += value
  else:
    # Invalid instruction
    raise ValueError(f"Invalid instruction: {instruction}")

  # Check if the current cycle is a signal strength checkpoint
  if (i + 1) % 40 == 20:
    signal += (i + 1) * x

# Print the final signal strength
print(signal)
"""

This code reads the input instructions from the `10_input` file and then loops through each instruction, executing it and updating the X register accordingly. After each instruction, the code checks if the current cycle is a signal strength checkpoint (i.e. the 20th, 60th, 100th, 140th, 180th, and 220th cycles), and if so, updates the signal strength by adding the product of the current cycle and the value of the X register. After all instructions have been executed, the code prints the final signal strength."""