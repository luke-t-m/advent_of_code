"""The following code can be used to solve the problem:

"""
# read input
with open('5_input') as f:
    lines = f.read().strip().split('\n')

# create list of stacks
stacks = [[c for c in line] for line in lines[:-1]]

# create list of operations
ops = [[int(x) for x in line.split()] for line in lines[-1:][0].split('\n')]

# apply operations to stacks
for op in ops:
    # move crate from op[2] to op[4]
    crate = stacks[op[2]-1].pop(op[1])
    stacks[op[4]-1].insert(op[3], crate)

# print top crate of each stack
print(''.join([stacks[i][-1] for i in range(len(stacks))]))
"""

To run the code, save it in a file called `solution.py` and run it with `python solution.py`. The output of the code will be the answer to the problem."""