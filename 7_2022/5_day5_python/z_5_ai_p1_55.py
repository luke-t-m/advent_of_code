"""The following is a correct Python solution to the problem:
"""
# parse the input file
with open('5_input') as f:
    lines = f.read().strip().split('\n')

# split the input lines into commands and stacks
commands = lines[1:]
stacks = lines[0].split()

# apply each command to the stacks
for command in commands:
    # split the command into parts
    parts = command.split()

    # extract the stack numbers and number of crates
    from_stack = int(parts[1]) - 1
    to_stack = int(parts[3]) - 1
    num_crates = int(parts[4])

    # move the crates from one stack to the other
    for i in range(num_crates):
        # move the top crate from the from_stack to the to_stack
        crates = stacks[from_stack].split(',')
        stacks[from_stack] = ','.join(crates[:-1])
        stacks[to_stack] = crates[-1] + ',' + stacks[to_stack]

    # remove the trailing comma from the stacks
    stacks = [stack.rstrip(',') for stack in stacks]

# print the final configuration of the stacks
print(''.join(stacks))
"""

To run the solution, save the code to a file named `solution.py` and run the following command:
"""
python solution.py
""""""