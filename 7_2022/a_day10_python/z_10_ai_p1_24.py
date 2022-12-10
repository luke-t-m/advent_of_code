"""To solve this problem, we need to write a program that simulates the CPU's execution of the instructions in the input program. The program should store the value of the X register at each cycle, and then compute the signal strength at the 20th, 60th, 100th, 140th, 180th, and 220th cycles by multiplying the cycle number by the value of the X register at that cycle. Finally, the program should print the sum of the computed signal strengths.

Here is an implementation in Python:

"""
# Read the input from the file "10_input"
with open("10_input") as f:
    lines = f.readlines()

# Parse the input
program = []
for line in lines:
    # Split the line on the space character to get the instruction and the argument
    instr, arg = line.strip().split(" ")
    # Convert the argument to an integer
    arg = int(arg)
    # Add the instruction and argument as a tuple to the program
    program.append((instr, arg))

# Set the initial value of the X register to 1
x = 1

# Initialize a list to store the value of the X register at each cycle
x_history = []

# Simulate the execution of the program
for cycle in range(1, 250):
    # Append the current value of the X register to the history
    x_history.append(x)

    # Get the next instruction to execute
    instr, arg = program[(cycle - 1) % len(program)]

    # Execute the instruction
    if instr == "noop":
        # Do nothing
        pass
    elif instr == "addx":
        # Add the argument to the X register
        x += arg

# Compute the signal strength at the specified cycles
signal_strengths = [cycle * x_history[cycle - 1] for cycle in [20, 60, 100, 140, 180, 220]]

# Print the sum of the computed signal strengths
print(sum(signal_strengths))
""""""