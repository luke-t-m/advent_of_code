"""To solve this problem, you need to read the instructions from the input file, execute them, and print the signal strength of the X register at the 20th cycle and every 40 cycles after that.

First, you need to read the instructions from the input file. You can do this by opening the file and reading the lines one by one. Here is how you can do it:

"""
with open("10_input", "r") as input_file:
    instructions = input_file.readlines()
"""

Next, you need to execute the instructions and keep track of the X register and the current cycle. To execute the instructions, you can use a `for` loop to iterate over the instructions and check the instruction type using an `if` statement. Here is an example:

"""
x = 1
cycle = 0
for instruction in instructions:
    if instruction == "noop":
        # do something
    elif instruction.startswith("addx"):
        # do something
"""

For the `noop` instruction, you just need to increment the cycle counter by 1. For the `addx` instruction, you need to extract the value from the instruction and add it to the X register. Here is how you can do that:

"""
x = 1
cycle = 0
for instruction in instructions:
    if instruction == "noop":
        cycle += 1
    elif instruction.startswith("addx"):
        value = int(instruction.split()[1])
        x += value
        cycle += 2
"""

Finally, you need to print the signal strength of the X register at the 20th cycle and every 40 cycles after that. You can do this by using an `if` statement to check if the current cycle is one of the desired cycles, and if so, printing the signal strength by multiplying the cycle number by the value of the X register. Here is an example:

"""
x = 1
cycle = 0
for instruction in instructions:
    if instruction == "noop":
        cycle += 1
    elif instruction.startswith("addx"):
        value = int(instruction.split()[1])
        x += value
        cycle += 2

    # Print the signal strength at the 20th, 60th, 100th, 140th, 180th, and 220th cycles
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength = cycle * x
        print(signal_strength)
"""

Putting it all together, you can solve this problem using the following Python code:

"""
with open("10_input", "r") as input_file:
    instructions = input_file.readlines()

x = 1
cycle = 0
for instruction in instructions:
    if instruction == "noop":
        cycle += 1
    elif instruction.startswith("addx"):
        value = int(instruction.split()[1])
        x += value
        cycle += 2

    # Print the signal strength at the 20th, 60th, 100th, 140th, 180th, and 220th cycles
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength = cycle * x
        print(signal_strength)
""""""