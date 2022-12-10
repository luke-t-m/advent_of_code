# Read from the file called 10_input
with open("10_input", "r") as file:
  instructions = file.readlines()

# Parse the instructions
instructions = [i.strip().split() for i in instructions]

# Initialize the register to 1
register = 1

# Initialize a list to store the signal strengths
signal_strengths = []

# Initialize the cycle counter to 0
cycle = 0

# Iterate over the instructions
for instruction in instructions:
  # If the instruction is a noop, increment the cycle counter by 1
  if instruction[0] == "noop":
    cycle += 1
  # If the instruction is an addx, increment the cycle counter by 2, and update the register
  elif instruction[0] == "addx":
    cycle += 2
    register += int(instruction[1])

  # If the cycle is a multiple of 20, add the current signal strength to the list
  if cycle % 20 == 0:
    signal_strengths.append(cycle * register)

# Print the signal strengths
print(signal_strengths)