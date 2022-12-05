"""The code for the solution to the problem is shown below:
"""
# Read the input from the file
with open('5_input', 'r') as f:
    input_lines = f.readlines()

# Get the number of stacks
num_stacks = len(input_lines)

# Initialize a list to hold the crates
crates = []

# For each line in the input
for line in input_lines:
    # Parse the line to get the crate
    crate = line.split(' ')[-1].strip()

    # Add the crate to the list
    crates.append(crate)

# Parse the input to get the rearrangement procedure
rearrangement_procedure = []
for line in input_lines:
    # Split the line by space
    parts = line.split(' ')

    # Get the number of crates to be moved
    num_crates = int(parts[0])

    # Get the source and destination stacks
    source_stack = int(parts[3])
    destination_stack = int(parts[5])

    # Add the move to the rearrangement procedure
    rearrangement_procedure.append((num_crates, source_stack, destination_stack))

# For each step in the rearrangement procedure
for step in rearrangement_procedure:
    # Unpack the step
    num_crates, source_stack, destination_stack = step

    # Remove the crates from the source stack
    crates_to_move = crates[source_stack - 1][:num_crates]
    crates[source_stack - 1] = crates[source_stack - 1][num_crates:]

    # Add the crates to the destination stack
    crates[destination_stack - 1] = crates_to_move + crates[destination_stack - 1]

# Print the top crate of each stack
for i in range(1, num_stacks + 1):
    print(crates[i - 1][0], end='')
""""""