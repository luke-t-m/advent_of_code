"""The following code can be used to solve the problem.
"""
# Open the file containing the input
with open('10_input') as f:
  # Read the lines from the file and store them in a list
  lines = f.readlines()

# Initialize the X register to 1
x = 1

# Loop through the instructions in the input
for line in lines:
  # Split the line into the instruction and the value
  instr, val = line.split()
  val = int(val)
  # If the instruction is "addx", add the value to the register
  if instr == "addx":
    x += val

# Calculate the signal strength during the 20th cycle and every 40 cycles after that
signal = 20 * x
signal += 40 * x
signal += 100 * x
signal += 140 * x
signal += 180 * x
signal += 220 * x

# Print the final signal strength
print(signal)
""""""