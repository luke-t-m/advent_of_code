"""Here is a solution to the problem in Python:

"""
# Read input from 10_input file
with open("10_input") as f:
    instructions = [line.strip() for line in f]

# Initialize X register and current instruction
x = 1
inst_ptr = 0

# Loop until all instructions are executed
while inst_ptr < len(instructions):
    # Get current instruction and its argument
    inst, arg = instructions[inst_ptr].split()
    arg = int(arg)

    # Execute the instruction
    if inst == "addx":
        x += arg
    elif inst == "noop":
        pass

    # Increment instruction pointer
    inst_ptr += 1

# Calculate signal strength
signal_strength = 0
for i in range(20, 240, 40):
    signal_strength += i * x

# Print the signal strength
print(signal_strength)
""""""