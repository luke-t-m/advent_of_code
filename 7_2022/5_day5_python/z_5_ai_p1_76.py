"""The following is a solution to the problem in Python.

"""
# Read the input
with open('5_input', 'r') as f:
    input = f.read().strip()

# Parse the input
input = input.split('\n')
stacks = input[:3]
stacks = [list(stack) for stack in stacks]
procedure = input[3:]

# Execute the procedure
for move in procedure:
    # Parse the move
    move = move.split()
    num_crates = int(move[1])
    from_stack = int(move[2]) - 1
    to_stack = int(move[5]) - 1

    # Perform the move
    moved_crates = stacks[from_stack][-num_crates:]
    stacks[from_stack] = stacks[from_stack][:-num_crates]
    stacks[to_stack] += moved_crates

# Print the top crates on each stack
print(''.join(stack[-1] for stack in stacks))
"""

To run this code, save it to a file called `5.py` and run it with `python 5.py`. It will print the answer to the problem."""