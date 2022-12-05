"""Here is a python solution to the problem:

"""
# Read the input from the file 5_input
with open("5_input") as file:
    input_str = file.read()

# Parse the input
stacks = [[crate for crate in line] for line in input_str.strip().split("\n")]

# Initialize the list of moves
moves = []

# Parse the moves
for line in input_str.strip().split("\n")[len(stacks):]:
    # Split the line into its components
    components = line.split()
    # Parse the quantity and the two stack indices
    qty, from_stack, _, _, _, to_stack = components
    # Append the move to the list
    moves.append((int(qty), int(from_stack), int(to_stack)))

# Perform the moves
for qty, from_stack, to_stack in moves:
    # Remove the top qty crates from the from_stack
    crates = stacks[from_stack - 1][-qty:]
    # Remove the crates from the from_stack
    stacks[from_stack - 1] = stacks[from_stack - 1][:-qty]
    # Add the crates to the to_stack
    stacks[to_stack - 1].extend(crates)

# Print the top crates of each stack
print("".join(stack[-1] for stack in stacks))
""""""