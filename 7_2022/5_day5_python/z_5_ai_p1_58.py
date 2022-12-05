"""The input must be read from a file called `5_input`. The first step is to read the file and store the input in a variable.

"""
with open("5_input") as f:
    input = f.read()
"""

The input is a sequence of instructions that specify how the crates are to be rearranged. The instructions are in the form `move x from y to z`, where `x` is the number of crates to move, `y` is the starting stack and `z` is the destination stack. To solve the problem, we need to simulate the rearrangement procedure by applying each instruction in turn and keeping track of the top crate on each stack.

First, we need to parse the input and extract the instructions. We can use a regular expression to match each instruction and store the instructions in a list.

"""
import re

instructions = []

for line in input.strip().split("\n"):
    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    if m:
        instructions.append(tuple(map(int, m.groups())))
"""

Next, we need to simulate the rearrangement procedure by applying each instruction in turn. We can do this by using a list to represent the stacks of crates, where each element in the list is a stack of crates. We will initialize the list with a single crate on each stack.

"""
stacks = [[c] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
"""

To apply each instruction, we will use the `pop()` and `insert()` methods to move the specified number of crates from the starting stack to the destination stack.

"""
for x, y, z in instructions:
    crates = [stacks[y-1].pop() for _ in range(x)]
    stacks[z-1].extend(crates)
"""

After all the instructions have been applied, we can print the top crate on each stack by using the `peek()` method to get the top element of each stack without removing it.

"""
print("".join(stack[-1] for stack in stacks))
"""

Putting it all together, we get the following solution:

"""
import re

with open("5_input") as f:
    input = f.read()

instructions = []

for line in input.strip().split("\n"):
    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    if m:
        instructions.append(tuple(map(int, m.groups())))

stacks = [[c] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

for x, y, z in instructions:
    crates = [stacks[y-1].pop() for _ in range(x)]
    stacks[z-1].extend(crates)

print("".join(stack[-1] for stack in stacks))
""""""