"""To solve this problem, we can first create a function that takes a string of instructions and the number of cycles to execute them. The function will split the instructions on newline characters to create a list of instructions, and then iterate over the instructions for the specified number of cycles. For each instruction, it will update the value of the X register according to the instruction, and keep track of the signal strength by multiplying the cycle number by the value of the X register. At the end, the function can print the signal strengths that were calculated.

Here is an example implementation in Python:

"""
def solve(instructions, num_cycles):
  # Split the instructions on newline characters to create a list of instructions
  instructions = instructions.strip().split('\n')

  # Initialize the X register with a value of 1
  x = 1

  # Iterate over the instructions for the specified number of cycles
  for i in range(num_cycles):
    # Get the current instruction
    instruction = instructions[i % len(instructions)]

    # Parse the instruction to determine the operation and value
    operation, value = instruction.split()
    value = int(value)

    # Update the X register according to the instruction
    if operation == 'addx':
      x += value

    # Keep track of the signal strength (cycle number * X register value)
    # during the 20th cycle and every 40 cycles after that
    if i == 20 or (i > 20 and (i - 20) % 40 == 0):
      print(i * x)


# Test the function with the given small program
instructions = """
noop
addx 3
addx -5
"""
solve(instructions, 240)

# Test the function with the given larger program
instructions = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1"""