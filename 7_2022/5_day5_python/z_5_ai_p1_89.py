"""First, create the input file.

"""
echo "[D]
[N] [C]
[Z] [M] [P]" > 5_input
"""

To solve the problem, you will need to parse the input file and apply the rearrangement steps.

First, read the input file and store it in a list of lists of strings.

"""
with open('5_input') as f:
    stacks = [list(line.strip()) for line in f.readlines()]
"""

Next, parse the rearrangement steps and apply them to the list of stacks.

"""
rearrangements = [
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]

for rearrangement in rearrangements:
    words = rearrangement.split()
    source = int(words[2]) - 1
    dest = int(words[4]) - 1
    crate = stacks[source].pop()
    stacks[dest].append(crate)
"""

Finally, print the top crate from each stack.

"""
print(''.join(stack[-1] for stack in stacks))
"""

Combining all the code together, you get the following solution:

"""
with open('5_input') as f:
    stacks = [list(line.strip()) for line in f.readlines()]

rearrangements = [
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]

for rearrangement in rearrangements:
    words = rearrangement.split()
    source = int(words[2]) - 1
    dest = int(words[4]) - 1
    crate = stacks[source].pop()
    stacks[dest].append(crate)

print(''.join(stack[-1] for stack in stacks))
""""""