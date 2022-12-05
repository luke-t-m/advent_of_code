"""The following is a correct python solution to the problem:

"""
# store the starting state of the stacks in a list
stacks = [['Z'], ['M', 'C', 'D'], ['P']]

# read the input file and parse the instructions
with open('5_input') as f:
    instructions = [line.strip().split() for line in f]

# execute the instructions
for instruction in instructions:
    # get the source and destination stacks
    source = int(instruction[1])
    dest = int(instruction[3])

    # move the top crate from the source stack to the top of the destination stack
    crate = stacks[source].pop()
    stacks[dest].append(crate)

# combine the top crates from each stack and print the result
result = ''.join([stacks[i][-1] for i in range(len(stacks))])
print(result)
""""""