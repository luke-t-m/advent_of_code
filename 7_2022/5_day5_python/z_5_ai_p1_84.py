"""Here is a solution to the problem written in Python:

"""
# read input from the file "5_input"
with open("5_input") as f:
    lines = f.readlines()

# parse the input
stacks = [[] for _ in range(3)]
for line in lines:
    parts = line.split()
    if parts[0] == "move":
        # parse a move command
        count = int(parts[1])
        from_stack = int(parts[2][1])
        to_stack = int(parts[5][1])
        # move the crates
        crates = stacks[from_stack-1][-count:]
        stacks[from_stack-1] = stacks[from_stack-1][:-count]
        stacks[to_stack-1].extend(crates)
    else:
        # parse a stack of crates
        stack = int(parts[0][1])
        crates = parts[1:]
        # add the crates to the appropriate stack
        stacks[stack-1].extend(crates)

# print the top crate from each stack
for stack in stacks:
    print(stack[-1], end="")
""""""