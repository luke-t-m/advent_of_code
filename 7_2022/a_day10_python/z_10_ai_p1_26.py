"""To solve this problem, we will first create a function `run_program` that takes a list of instructions and a starting value for the register `X`, and returns the final value of `X` after executing all the instructions. The function will iterate over the instructions, executing each instruction by updating the value of `X` according to the instruction.

Here is an example implementation:

"""
def run_program(instructions, X):
    for instruction in instructions:
        if instruction.startswith('addx'):
            # Parse the value to add from the instruction string
            value_to_add = int(instruction.split()[1])
            # Update the value of X
            X += value_to_add
    return X
"""

We can then use this function to solve the problem. We will read the instructions from the input file `10_input`, run the program using these instructions and a starting value of `X=1`, and compute the signal strength of the program by multiplying the value of `X` by the cycle number for the 20th, 60th, 100th, 140th, 180th, and 220th cycles. Here is how this can be done:

"""
# Read the instructions from the input file
with open('10_input') as f:
    instructions = f.read().strip().split('\n')

# Run the program
X = run_program(instructions, 1)

# Compute the signal strength for the 20th, 60th, 100th, 140th, 180th, and 220th cycles
signal_strength = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    signal_strength += X * cycle

# Print the final signal strength
print(signal_strength)
"""

This should solve the problem."""