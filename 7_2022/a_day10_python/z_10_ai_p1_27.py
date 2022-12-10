"""Here is a possible solution to the problem in Python:

"""
# Read the program from the input file
with open("10_input", "r") as f:
    program = [line.strip() for line in f]

# Initialize the X register
x = 1

# Initialize the clock
clock = 0

# Initialize the signal strengths
signal_strengths = []

# Execute the program
for instr in program:
    # Parse the instruction
    op, val = instr.split()
    val = int(val)

    # Increment the clock
    clock += 1

    # Execute the instruction
    if op == "addx":
        x += val
    elif op == "noop":
        pass

    # Update the signal strengths
    if clock == 20 or (clock > 20 and clock % 40 == 0):
        signal_strengths.append(clock * x)

# Print the final signal strengths
print(signal_strengths)
""""""