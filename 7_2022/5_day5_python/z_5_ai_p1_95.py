"""The following code should solve the problem.

"""
# Read the input from the file 5_input
with open('5_input', 'r') as file:
    input = file.read()

# Parse the input to get the initial stack configuration and the movement instructions
lines = input.strip().split('\n')
stacks = [[crate for crate in stack] for stack in lines[:3]]
instructions = [tuple(line.split()) for line in lines[3:]]

# Apply the instructions
for instruction in instructions:
    source_stack, source_index, target_stack, target_index = instruction
    # Parse the indexes
    source_index = int(source_index.strip('()')) - 1
    target_index = int(target_index.strip('()')) - 1
    # Move the crate from the source stack to the target stack
    crate = stacks[source_stack][source_index]
    stacks[source_stack] = stacks[source_stack][:source_index] + stacks[source_stack][source_index + 1:]
    stacks[target_stack] = stacks[target_stack][:target_index] + [crate] + stacks[target_stack][target_index:]

# Print the top crates in each stack
for stack in stacks:
    print(stack[-1], end='')
"""

After running this code, the top crates in each stack should be printed."""