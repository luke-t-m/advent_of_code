""""""
stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

while True:
    # read move instructions
    instr = input()
    if instr == '':
        break

    # parse instructions
    instr = instr.split()
    n = int(instr[1])
    from_stack = int(instr[2])
    to_stack = int(instr[5])

    # move crates
    for i in range(n):
        crate = stacks[from_stack-1].pop()
        stacks[to_stack-1].append(crate)

# print top crate of each stack
for stack in stacks:
    print(stack[-1], end='')
"""

Note that the input must be read from a file called `5_input`.
To do this, you can use the following code at the top of the script:
"""
with open('5_input') as f:
    instr = f.read().strip()
"""
Then, you can use the `input()` function to read each line of the input."""