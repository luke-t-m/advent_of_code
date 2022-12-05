"""To solve this problem, we need to simulate the sequence of movements given in the input. We can use a list to represent the stacks of crates, where the first element of the list is the top crate of the first stack, the second element is the top crate of the second stack, and so on. To move a crate from one stack to another, we can simply remove the top crate from the source stack and append it to the destination stack.

Here is one way to solve this problem in Python:

"""
# Read the input
with open("5_input") as f:
    lines = f.read().strip().split("\n")

# Parse the input
stacks = [list(stack) for stack in lines[0].split()]
moves = [line.split() for line in lines[1:]]

# Apply the moves
for move in moves:
    # Parse the move
    n_crates = int(move[0])
    src_stack = int(move[1].split("from")[1]) - 1
    dest_stack = int(move[3]) - 1

    # Move the crates
    crates = [stacks[src_stack].pop() for _ in range(n_crates)]
    for crate in crates:
        stacks[dest_stack].append(crate)

# Print the final configuration of the stacks
print("".join([stacks[i][-1] for i in range(len(stacks))]))
"""

The output of this program will be the final configuration of the stacks, with the top crate of each stack concatenated together, as required by the problem statement."""