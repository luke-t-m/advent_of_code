"""To solve this problem, we need to read the starting configuration of the stacks of crates, and the list of moves to be performed, and apply the moves to the stacks. After all the moves have been applied, we can then determine the top crate of each stack.

Here is one way to solve this problem in Python:

"""
# Read the input from the file called 5_input
with open('5_input') as f:
    lines = f.readlines()

# Parse the input
# The first line contains the starting configuration of the stacks
stacks = [[c for c in line.strip()] for line in lines[0:3]]
# The remaining lines contain the moves to be performed
moves = [line.strip() for line in lines[3:]]

# Perform the moves
for move in moves:
    # Parse the move
    words = move.split()
    n = int(words[1])
    from_stack = int(words[2])
    to_stack = int(words[5])

    # Move the top n crates from from_stack to to_stack
    crates = stacks[from_stack-1][:n]
    stacks[from_stack-1] = stacks[from_stack-1][n:]
    stacks[to_stack-1] = crates + stacks[to_stack-1]

# Determine the top crates of each stack
top_crates = [stack[-1] for stack in stacks]

# Print the answer
print(''.join(top_crates))
"""

This code reads the input from a file called `5_input`, and uses a loop to apply each move to the stacks. After all the moves have been applied, it determines the top crate of each stack and prints the answer."""