"""To solve this problem, we need to execute the instructions in the given program and compute the signal strength as described in the prompt. Below is a Python solution that does that:

"""
# Read instructions from file
with open('10_input') as f:
    instructions = [line.strip() for line in f]

# Initialize variables
x = 1
cycle = 0
signal_strength = 0

# Loop until the 220th cycle
while cycle < 220:
    # Parse the current instruction
    instr, *args = instructions[cycle % len(instructions)].split()
    value = int(args[0]) if args else None

    # Execute the instruction
    if instr == 'addx':
        x += value
    elif instr == 'noop':
        pass

    # Compute the signal strength
    if cycle in (19, 59, 99, 139, 179, 219):
        signal_strength += cycle * x

    # Move to the next cycle
    cycle += 1

# Print the final signal strength
print(signal_strength)
""""""