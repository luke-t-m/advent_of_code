"""The following is the solution to the problem in Python.

"""
# read input
with open('5_input', 'r') as f:
    lines = f.readlines()

# parse input
stacks = [list(line.strip()) for line in lines[1:]]
instructions = lines[0].strip().split('\n')

# rearrange the crates
for instruction in instructions:
    words = instruction.split()
    num_crates = int(words[1])
    from_stack = int(words[3]) - 1
    to_stack = int(words[5]) - 1
    crates = stacks[from_stack][:num_crates]
    stacks[from_stack] = stacks[from_stack][num_crates:]
    stacks[to_stack] = crates + stacks[to_stack]

# print the top crates of each stack
for stack in stacks:
    print(stack[-1], end='')
""""""