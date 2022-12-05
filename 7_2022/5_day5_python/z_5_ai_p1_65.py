"""Here is a solution in python:

"""
# read the input from the file
with open('5_input') as f:
    lines = f.readlines()

# get the initial configuration of the crates from the input
crates = lines[:3]

# remove leading and trailing whitespace from the crates
crates = [crate.strip() for crate in crates]

# parse the rearrangement instructions from the input
instructions = lines[3:]

# for each instruction, perform the corresponding crate rearrangement
for instruction in instructions:
    # split the instruction into tokens
    tokens = instruction.split()
    # get the number of crates to move and the source and destination stacks
    num_crates = int(tokens[1])
    src_stack = int(tokens[2])
    dest_stack = int(tokens[5])

    # move the crates from the source stack to the destination stack
    # we do this by removing the top `num_crates` crates from the source stack and adding them to the destination stack
    crates[dest_stack - 1] += crates[src_stack - 1][-num_crates:]
    crates[src_stack - 1] = crates[src_stack - 1][:-num_crates]

# print the final configuration of the crates
print(''.join(crate[-1] for crate in crates))
""""""