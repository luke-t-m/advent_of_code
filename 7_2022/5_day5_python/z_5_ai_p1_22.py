"""The problem asks for the crates that end up on top of each stack after the rearrangement procedure. The input is a description of the stacks and the rearrangement procedure.

First, we need to parse the input to create the stacks and the procedure. Then, we can simulate the rearrangement, and finally output the crates that end up on top of each stack.

Here is a solution in Python:

"""
# Parse the input
with open("5_input") as f:
    lines = f.read().strip().split("\n")

# Create the stacks
stacks = [list(line) for line in lines[:-1]]

# Create the rearrangement procedure
procedure = []
for line in lines[-1:]:
    words = line.split()
    procedure.append((int(words[1]), int(words[3]), int(words[5])))

# Simulate the rearrangement
for a, b, c in procedure:
    stacks[c-1].append(stacks[a-1].pop(b-1))

# Output the crates that end up on top of each stack
print("".join(stack[-1] for stack in stacks))
""""""