"""The code below will solve the problem as described in the prompt.

"""
import sys

# read input from file
with open("10_input", "r") as f:
    input_str = f.read()

# parse input
instructions = input_str.strip().split("\n")

# initialize the register with value 1
x = 1

# initialize cycle count with 0
cycle_count = 0

# initialize a list to store signal strength
signal_strength = []

# iterate over instructions
for instr in instructions:

    # split instruction and value
    instr, val = instr.split(" ")

    # convert value to int
    val = int(val)

    # check instruction and execute
    if instr == "addx":
        x += val
    elif instr == "noop":
        pass

    # increment cycle count
    cycle_count += 1

    # check if current cycle is 20th or a multiple of 40
    if cycle_count == 20 or cycle_count % 40 == 0:

        # append signal strength to list
        signal_strength.append(cycle_count * x)

# print the answer
print(sum(signal_strength))
""""""