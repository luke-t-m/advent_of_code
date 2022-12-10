"""To solve this problem, you need to write a python program that simulates the execution of the instructions provided in the input file. The program should calculate the value of the X register for every 20th and every 40th cycle after the 20th cycle, and multiply it by the cycle number.

Here is an example solution:

"""
# Read the input file
with open("10_input") as f:
    instructions = [line.strip() for line in f.readlines()]

# Initialize the X register and the cycle counter
x = 1
cycle = 0

# Loop through the instructions
for instruction in instructions:
    # Increment the cycle counter
    cycle += 1
    
    # Split the instruction into the operation and the value
    op, val = instruction.split(" ")
    val = int(val)

    # If the operation is "addx", increment the X register
    # by the given value
    if op == "addx":
        x += val

    # If the operation is "noop", do nothing
    elif op == "noop":
        pass

    # If the current cycle is a multiple of 20 or 40,
    # print the value of the X register multiplied by the cycle number
    if cycle % 20 == 0 or cycle % 40 == 0:
        print(x * cycle)
""""""