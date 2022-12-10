"""To solve this problem, you will need to read the instructions from the file `10_input`. You can read the instructions using the `open` function and read the lines using a `for` loop. Then, you can execute the instructions by updating a variable `X` according to the instructions. To get the signal strength, you need to multiply `X` by the cycle number for each cycle that is a multiple of 20 or 40. You can use the `%` operator to check if a number is a multiple of 20 or 40. Finally, you can print the answer by summing up the signal strength for each cycle.

Here is an example of how you can solve this problem in Python:

"""
# Open the input file
with open("10_test") as f:
    # Read the instructions from the input file
    instructions = [line.strip() for line in f]

# Initialize the X register with the value 1
X = 1

# Initialize the signal strength to 0
signal_strength = 0

# Loop over the instructions
for i, instruction in enumerate(instructions):
    # Check if the current cycle is a multiple of 20 or 40
    if (i + 1) % 20 == 0:
        # Update the signal strength by multiplying X by the current cycle
        signal_strength += X * (i + 1)

    # Check if the instruction is "noop"
    if instruction == "noop":
        # Do nothing
        pass
    else:
        # Split the instruction into the operation and the operand
        op, operand = instruction.split()

        # Check if the operation is "addx"
        if op == "addx":
            # Update the value of X by adding the operand
            X += int(operand)

# Print the answer
print(signal_strength)
""""""