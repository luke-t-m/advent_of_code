"""To solve this problem, we need to simulate the execution of the instructions in the program. We will do this by iterating through the instructions in the program and updating the value of the `X` register according to the instructions.

First, we need to read the instructions from the input file. We can do this with the following code:

"""
# Open the input file
with open('10_input', 'r') as f:
    # Read the instructions from the file, splitting on the newline character
    instructions = f.read().split('\n')

# Remove any empty instructions from the list
instructions = [i for i in instructions if i]
"""

Next, we need to simulate the execution of the instructions. We can do this with a `while` loop that continues until we reach the end of the instructions. Inside the loop, we will check the current instruction and update the value of the `X` register accordingly.

"""
# Initialize the X register with a value of 1
x = 1

# The current instruction number (we start at 1 since the first instruction is executed during the first cycle)
instruction_num = 1

# The signal strength (the product of the instruction number and the value of the X register)
signal_strength = 0

# The cycle number (we start at 1 since the first cycle is the first time an instruction is executed)
cycle_num = 1

# A list to store the signal strengths during the 20th, 60th, 100th, etc. cycles
signal_strengths = []

# Loop until we reach the end of the instructions
while instruction_num <= len(instructions):
    # Get the current instruction
    instruction = instructions[instruction_num - 1]

    # Check the instruction
    if instruction == 'noop':
        # Do nothing (the noop instruction has no effect on the X register)
        pass
    elif instruction.startswith('addx'):
        # Parse the value to add from the instruction
        value = int(instruction.split(' ')[1])

        # Update the X register
        x += value

    # Update the signal strength and the cycle number
    signal_strength = instruction_num * x
    cycle_num += 1

    # Check if we are at the 20th, 60th, 100th, etc. cycle
    if cycle_num % 40 == 0:
        # If so, store the signal strength
        signal_strengths.append(signal_strength)

    # Move to the next instruction
    instruction_num += 1
"""

Finally, we can print the answer by printing the sum of the signal strengths during the 20th, 60th, 100th, etc. cycles.

"""
# Print the sum of the signal strengths during the 20th, 60th, 100th, etc. cycles
print(sum(signal_strengths))
"""

Putting it all together, we get the following solution:

"""
# Open the input file
with open('10_input', 'r') as f:
    # Read the instructions from the file, splitting on the newline character
    instructions = f.read().split('\n')

# Remove any empty instructions from the list
instructions = [i for i in instructions if i]

# Initialize the X register with a value of 1
x = 1
