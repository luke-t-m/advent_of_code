"""The following is a solution to the above problem written in Python:

"""
# open the input file and read its contents
with open("5_input") as f:
    contents = f.read()

# split the input into a list of lines
lines = contents.split("\n")

# get the starting stacks and the rearrangement procedure from the input
starting_stacks = lines[:3]
rearrangement_procedure = lines[3:]

# initialize the current stacks to be the starting stacks
current_stacks = starting_stacks

# go through each step in the rearrangement procedure
for step in rearrangement_procedure:
    # split the step into its individual parts
    parts = step.split(" ")

    # get the number of crates to move, the starting stack, and the ending stack
    num_crates = int(parts[1])
    start_stack = int(parts[3])
    end_stack = int(parts[5])

    # move the crates from the starting stack to the ending stack
    crates_to_move = current_stacks[start_stack][:num_crates]
    current_stacks[start_stack] = current_stacks[start_stack][num_crates:]
    current_stacks[end_stack] = crates_to_move + current_stacks[end_stack]

# print the final stack, which is the crate that ends up on top of each stack
print(current_stacks)
""""""