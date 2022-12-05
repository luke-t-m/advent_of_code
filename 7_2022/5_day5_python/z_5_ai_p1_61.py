"""
# Read the input from file
with open('5_input') as file:
    data = file.read()

# Convert the data into a list of lists
crates = [list(stack) for stack in data.strip().split('\n')]

# Move the crates according to the instructions
for move in moves:
    # Parse the move
    from_stack, _, count, _, _, _, to_stack = move.split()
    
    # Move the crates
    crates[int(to_stack) - 1] += crates[int(from_stack) - 1][-int(count):]
    crates[int(from_stack) - 1] = crates[int(from_stack) - 1][:-int(count)]

# Print the top crate in each stack
for stack in crates:
    print(stack[-1], end='')
"""