"""To solve this problem, we need to execute the given program and print the signal strength of the X register during the 20th cycle and every 40 cycles after that.

First, we need to parse the input and store it in a list of tuples, where each tuple represents an instruction and contains the instruction name and its value.

Next, we need to execute the instructions in the program, keeping track of the value of the X register and the current cycle. When we reach the 20th cycle, we need to print the signal strength of the X register, and then continue executing the program and printing the signal strength every 40 cycles after that.

Here is a possible solution in Python:

"""
# Parse the input and store it in a list of tuples
instructions = []
with open("10_input") as f:
    for line in f:
        instr, val = line.strip().split()
        instructions.append((instr, int(val)))

# Initialize the X register and the current cycle
x = 1
cycle = 0

# Execute the instructions in the program
for instr, val in instructions:
    if instr == "addx":
        # If the instruction is "addx", increase the X register by the given value
        x += val
    elif instr == "noop":
        # If the instruction is "noop", do nothing
        pass

    # Increment the current cycle
    cycle += 1

    # If we have reached the 20th cycle or a multiple of 40 thereafter, print the signal strength
    if cycle == 20 or cycle % 40 == 0:
        print(cycle * x)
"""

Note that this solution assumes that the input is well-formed and contains only valid instructions. It also doesn't handle any exceptional cases, such as invalid instructions or negative values for the "addx" instruction. These issues should be handled in a production-grade solution."""