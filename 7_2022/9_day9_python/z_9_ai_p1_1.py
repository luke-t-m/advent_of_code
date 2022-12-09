"""The problem asks you to model the movement of the head and tail of a rope. The head moves according to a series of instructions (R 4 means move the head right 4 steps). After each movement, you need to update the position of the tail according to the rules described in the problem statement.

First, let's read the instructions from the input file:

"""
with open('9_input') as f:
    instructions = f.readlines()
"""

Next, let's define the initial position of the head and tail:

"""
head = (0, 0)
tail = (0, 0)
"""

Now, let's iterate over the instructions and update the position of the head according to each instruction:

"""
for instr in instructions:
    direction, steps = instr[0], int(instr[1:])
    if direction == 'R':
        head = (head[0], head[1] + steps)
    elif direction == 'L':
        head = (head[0], head[1] - steps)
    elif direction == 'U':
        head = (head[0] - steps, head[1])
    elif direction == 'D':
        head = (head[0] + steps, head[1])
"""

After each movement of the head, we need to update the position of the tail according to the rules described in the problem statement. If the head and tail are not touching and are not in the same row or column, the tail always moves one step diagonally to keep up. Otherwise, if the head is two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough. Otherwise, the tail remains in the same position. We can implement these rules as follows:

"""
for instr in instructions:
    direction, steps = instr[0], int(instr[1:])
    if direction == 'R':
        head = (head[0], head[1] + steps)
    elif direction == 'L':
        head = (head[0], head[1] - steps)
    elif direction == 'U':
        head = (head[0] - steps, head[1])
    elif direction == 'D':
        head = (head[0] + steps, head[1])

    # Update the position of the tail
    if abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 0:
        tail = (tail[0] + (head[0] - tail[0]) // 2, tail[1])
    elif abs(head[1] - tail[1]) == 2 and abs(head[0] - tail[0]) == 0:
        tail = (tail[0], tail[1] + (head[1] - tail[1]) // 2)
    elif head[0] != tail[0] and head[1] != tail[1]:
        if head[0] > tail[0]:
            tail = (tail[0] + 1, tail[1])
        elif head[0] < tail[0]:
            tail = (tail[0] - 1, tail[1])
        if head[1] > tail[1]:
            tail = (tail[0], tail[1] + 1"""