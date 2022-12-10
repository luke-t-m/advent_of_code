"""To solve this problem, you will need to simulate the execution of the instructions in the CPU. You can do this by creating a function that takes a list of instructions and a register `X`. The function should simulate the execution of the instructions and return the value of `X` after all instructions have been executed.

Here is an example of how the function could be implemented in Python:

"""
def execute_instructions(instructions, X):
  for instruction in instructions:
    if instruction.startswith("noop"):
      # No operation, do nothing
      pass
    elif instruction.startswith("addx"):
      # Parse the value to add from the instruction
      value_to_add = int(instruction.split(" ")[1])
      X += value_to_add
  return X
"""

You can then use this function to solve the problem by reading the instructions from the input file and calling the `execute_instructions` function with the instructions and an initial value of `X=1`. Finally, you can compute the signal strength at the specified cycles by multiplying the value of `X` by the cycle number.

Here is an example of how you could use the `execute_instructions` function to solve the problem:

"""
# Read the instructions from the input file
with open("10_input") as f:
  instructions = [line.strip() for line in f]

# Initialize the register X with the value 1
X = 1

# Execute the instructions
X = execute_instructions(instructions, X)

# Compute the signal strength at the specified cycles
signal_strength = X * 20
print(signal_strength)
"""

Note that the code above only computes the signal strength at the 20th cycle. You will need to compute the signal strength at every 40 cycles after the 20th cycle as well. To do this, you can use a `for` loop that iterates over the specified cycles and computes the signal strength at each cycle by multiplying the value of `X` by the cycle number.

Here is an example of how you could use a `for` loop to compute the signal strength at the specified cycles:

"""
# Read the instructions from the input file
with open("10_input") as f:
  instructions = [line.strip() for line in f]

# Initialize the register X with the value 1
X = 1

# Execute the instructions
X = execute_instructions(instructions, X)

# Compute the signal strength at the specified cycles
for cycle in [20, 60, 100, 140, 180, 220]:
  signal_strength = X * cycle
  print(signal_strength)
"""

You can then print the signal strength at each of the specified cycles to solve the problem."""