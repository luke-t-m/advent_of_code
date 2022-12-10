"""To solve this problem, we need to write a program that can simulate the execution of the instructions in the input file. The program should keep track of the value of the X register and the cycle number, and it should print the signal strength of X during the 20th cycle and every 40 cycles after that.

To simulate the execution of the instructions, we can use a `while` loop that continues until the end of the program. Inside the loop, we can read the next instruction and execute it. If the instruction is `addx V`, we can increment the value of the X register by `V`. If the instruction is `noop`, we can do nothing.

At the end of each iteration of the loop, we can increment the cycle number and check if it is the 20th cycle or a multiple of 40. If it is, we can print the signal strength of X by multiplying the value of X by the cycle number.

Here is one way we could implement this in Python:

"""
# Read the instructions from the input file
with open("10_input", "r") as f:
    instructions = [line.strip() for line in f]

# Initialize the X register and the cycle number
x = 1
cycle = 0

# Continue until the end of the program
while instructions:
    # Get the next instruction
    instruction = instructions.pop(0)
    
    # Parse the instruction
    parts = instruction.split()
    if parts[0] == "addx":
        # Increment the X register by the specified value
        x += int(parts[1])
    else:
        # The instruction is "noop", do nothing
        pass
    
    # Increment the cycle number
    cycle += 1
    
    # Check if this is the 20th cycle or a multiple of 40
    if cycle in [20, 60, 100, 140, 180, 220]:
        # Print the signal strength of X
        print(cycle * x)
"""

This program should solve the problem and print the correct answer."""