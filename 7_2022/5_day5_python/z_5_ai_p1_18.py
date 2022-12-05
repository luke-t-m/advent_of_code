"""Here is a possible solution in Python:

"""
# read input from file
with open('5_input') as f:
    instructions = f.read().strip().split('\n')

# initialize the stacks of crates
stacks = [['Z'], ['M'], ['P']]

# apply each instruction in the input
for instruction in instructions:
    # parse the instruction into its parts
    words = instruction.split()
    n = int(words[1])
    from_stack = int(words[3]) - 1
    to_stack = int(words[5]) - 1

    # move n crates from the 'from_stack' to the 'to_stack'
    crates = stacks[from_stack][:n]
    stacks[from_stack] = stacks[from_stack][n:]
    stacks[to_stack] = crates + stacks[to_stack]

# print the top crate in each stack
print(''.join([stacks[i][-1] for i in range(len(stacks))]))
""""""