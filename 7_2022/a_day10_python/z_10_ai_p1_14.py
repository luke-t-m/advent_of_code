"""To solve this problem, you will need to write a program that simulates the execution of the instructions given in the problem description. The program should print the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.

Here is an example of how your program could be implemented in Python:

"""
# Read input from the file "10_input"
with open("10_input", "r") as f:
    instructions = f.readlines()

# Parse the instructions into a list of tuples
instructions = [tuple(inst.strip().split(" ")) for inst in instructions]

# Initialize the X register with the value 1
X = 1

# Loop through the instructions, executing each one in turn
for i, inst in enumerate(instructions):
    # If the instruction is "noop", do nothing
    if inst[0] == "noop":
        continue
    # If the instruction is "addx", update the value of X
    elif inst[0] == "addx":
        X += int(inst[1])
    # Print the signal strength every 40 cycles, starting at the 20th cycle
    if (i + 1) % 40 == 20:
        print((i + 1) * X)
""""""