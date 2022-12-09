"""The following code will solve the problem:

"""
# read input file
with open("9_input") as f:
    instructions = f.readlines()

# initial positions for head and tail
head_x, head_y = 0, 0
tail_x, tail_y = 0, 0

# loop through instructions
for instruction in instructions:
    # read direction and number of steps
    direction, steps = instruction[0], int(instruction[1:])

    # update position of head
    if direction == "R":
        head_x += steps
    elif direction == "L":
        head_x -= steps
    elif direction == "U":
        head_y += steps
    elif direction == "D":
        head_y -= steps

    # update position of tail
    # if head and tail are in the same row or column, tail follows head
    if head_x == tail_x or head_y == tail_y:
        tail_x, tail_y = head_x, head_y
    # otherwise, tail moves one step diagonally to keep up
    else:
        tail_x += 1 if head_x > tail_x else -1
        tail_y += 1 if head_y > tail_y else -1

# print final position of head
print(head_x, head_y)
""""""