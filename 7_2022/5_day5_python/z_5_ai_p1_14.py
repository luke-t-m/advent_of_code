"""Here is a solution to the problem. Note that the input file should be placed in the same directory as this script for it to work properly.

"""
# Read the input file
with open('5_input', 'r') as f:
    lines = f.readlines()

# Initialize the stacks of crates
stacks = [[] for _ in range(3)]

# Parse the input to populate the stacks
for line in lines:
    if line[0] == '[':
        # This is the starting configuration of the stacks
        crates = line.strip().split(' ')
        stacks[0].append(crates[0][1])
        stacks[1].append(crates[1][1])
        stacks[2].append(crates[2][1])
    else:
        # This is a movement instruction
        tokens = line.strip().split(' ')
        # Parse the instruction
        n = int(tokens[0])
        source = int(tokens[3])
        dest = int(tokens[5])
        # Move the crates from the source stack to the destination stack
        for _ in range(n):
            crates[dest - 1].append(crates[source - 1].pop())

# Print the top crates of each stack
print(''.join(stacks[0][-1:] + stacks[1][-1:] + stacks[2][-1:]))
""""""