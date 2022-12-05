"""#!/usr/bin/python

with open('5_input') as f:
    stacks = []
    for line in f:
        line = line.strip()
        if line:
            stacks.append(list(line))

for i in range(1, len(stacks[-1])):
    line = stacks[-1][i]
    if line[0] == 'm':
        from_stack = int(line[5])
        to_stack = int(line[-1])
        crates = stacks[from_stack-1].pop()
        stacks[to_stack-1].append(crates)
    elif line[0] == 'p':
        from_stack = int(line[5])
        crates = stacks[from_stack-1].pop()
        stacks[-1].append(crates)

print(''.join(stacks[-1]))"""