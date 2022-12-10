"""The code below will solve the problem.

"""
# Open the input file and read the instructions
with open("10_input", "r") as file:
    instructions = file.readlines()

# Parse the instructions into a list of tuples
instructions = [tuple(inst.split()) for inst in instructions]

# Initialize the register to 0
x = 0

# Execute each instruction
for instruction in instructions:
    # If the instruction is "addx", add the value to the register
    if instruction[0] == "addx":
        x += int(instruction[1])

# Compute and print the signal strength
signal_strength = x * len(instructions)
print(signal_strength)
""""""