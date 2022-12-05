"""Here's a simple solution in Python:

"""
# read input
with open("5_input") as f:
    lines = f.readlines()

# split input into two parts: initial state and steps
initial_state = lines[:3]
steps = lines[3:]

# parse initial state into list of stacks
stacks = []
for line in initial_state:
    stacks.append(list(line.strip()))

# simulate steps
for step in steps:
    # parse step into source and destination stacks
    source, _, _, dest = step.split()
    source = int(source)
    dest = int(dest)

    # move top crate from source stack to destination stack
    crate = stacks[source - 1].pop()
    stacks[dest - 1].append(crate)

# print top crates of each stack
print("".join([stacks[i][-1] for i in range(3)]))
""""""