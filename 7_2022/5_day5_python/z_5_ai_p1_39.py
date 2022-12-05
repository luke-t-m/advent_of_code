"""To solve this problem, you can use the following Python code:

"""
# Read the input
with open("5_input") as f:
    moves = f.readlines()

# Initialize the stacks
stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]

# Perform the moves
for move in moves:
    # Parse the move
    num, from_stack, _, _, to_stack = move.split()
    num = int(num)

    # Move the crates
    for i in range(num):
        crate = stacks[int(from_stack) - 1].pop()
        stacks[int(to_stack) - 1].append(crate)

# Print the top crates of each stack
for stack in stacks:
    print(stack[-1], end="")
"""

This code reads the input from a file called `5_input`, then performs the moves on the stacks of crates. Finally, it prints the top crate of each stack."""