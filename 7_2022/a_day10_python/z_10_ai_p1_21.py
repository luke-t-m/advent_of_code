"""To solve this problem, you can create a function that reads the input from the `10_input` file and processes each instruction. For each instruction, update the value of the `X` register accordingly. Then, for each cycle in the range of 20, 60, 100, 140, 180, and 220, multiply the cycle number by the value of the `X` register and print the result.

Here is an example solution in Python:

"""
def solve():
    # Read the input from the file
    with open("10_input", "r") as f:
        instructions = f.readlines()

    # Initialize the X register
    x = 1

    # Loop through each instruction
    for instruction in instructions:
        # Split the instruction into its parts
        instr, val = instruction.strip().split()
        val = int(val)

        # Update the X register based on the instruction
        if instr == "addx":
            x += val
        elif instr == "noop":
            # noop does nothing
            pass

    # Loop through the specified cycles
    for cycle in [20, 60, 100, 140, 180, 220]:
        # Print the result of the calculation for the current cycle
        print(cycle * x)

# Call the function to solve the problem
solve()
""""""