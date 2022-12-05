"""The following code should solve the problem described above.

"""
# read input
with open('5_input') as f:
    moves = f.readlines()

# initialize stacks
stacks = [['Z'], ['M'], ['P']]

# process moves
for move in moves:
    parts = move.split()
    n = int(parts[1])
    src = int(parts[2])
    dest = int(parts[5])

    # remove n crates from src stack
    crates = stacks[src-1][:n]

    # add crates to dest stack
    stacks[dest-1] = crates + stacks[dest-1]

# get top crates from each stack
top_crates = [stack[0] for stack in stacks]

# combine and print top crates
print(''.join(top_crates))
""""""