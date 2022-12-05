"""Here is a solution to the problem in Python:

"""
# Read the input from the file
with open('5_input', 'r') as file:
    stacks = []
    for line in file:
        stack = line.split()
        stacks.append(stack)

# Process the moves
for move in moves:
    # Parse the move
    words = move.split()
    num_crates = int(words[0])
    from_stack = int(words[3]) - 1
    to_stack = int(words[5]) - 1

    # Move the crates
    for i in range(num_crates):
        crates[to_stack].append(crates[from_stack].pop())

# Print the top crates
for stack in stacks:
    print(stack[-1], end='')
""""""