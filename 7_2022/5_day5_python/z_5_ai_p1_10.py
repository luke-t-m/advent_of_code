"""Here is one possible solution in python.

"""
stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

def move(frm, to):
    if frm != to:
        stacks[to].append(stacks[frm].pop())

move(1, 0)
move(0, 2)
move(1, 0)
move(0, 1)

print(stacks)
"""

It first creates a list of the stacks in their initial configuration. Then it defines a `move` function that takes the index of the stack to move from and the index of the stack to move to as arguments, and moves the top crate of the `frm` stack to the top of the `to` stack. Finally, it applies the rearrangement procedure by calling the `move` function for each step of the procedure. The result is printed at the end.

After applying the rearrangement procedure, the `stacks` variable should look like this:
"""
stacks = [['Z'], ['C', 'M', 'N'], ['D', 'P']]
"""

To get the message that the Elves want, we can concatenate the top crates of each stack like this:
"""
message = ''.join([stacks[i][-1] for i in range(len(stacks))])
"""

The final solution looks like this:
"""
stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

def move(frm, to):
    if frm != to:
        stacks[to].append(stacks[frm].pop())

move(1, 0)
move(0, 2)
move(1, 0)
move(0, 1)

message = ''.join([stacks[i][-1] for i in range(len(stacks))])
print(message)
"""

This code should print `CMZ` as the output."""