"""The code for this problem is as follows:

"""
# Read input from file
with open('9_input', 'r') as f:
    steps = f.readlines()

# Initialize variables
x = 0
y = 0
tail_x = 0
tail_y = 0

# Loop over steps
for step in steps:
    # Parse direction and distance
    direction = step[0]
    distance = int(step[1:])

    # Update position based on direction
    if direction == 'R':
        x += distance
    elif direction == 'L':
        x -= distance
    elif direction == 'U':
        y += distance
    elif direction == 'D':
        y -= distance

    # Update position of tail
    dx = abs(x - tail_x)
    dy = abs(y - tail_y)
    if dx == 0 and dy == 0:
        # Do nothing (head and tail overlap)
        pass
    elif dx <= 2 and dy <= 2:
        # Move tail one step in the same direction as the head
        tail_x += distance if x > tail_x else -distance
        tail_y += distance if y > tail_y else -distance
    else:
        # Move tail one step diagonally to keep up with head
        tail_x += distance if x > tail_x else -distance
        tail_y += distance if y > tail_y else -distance

# Print final position of tail
print(tail_x, tail_y)
""""""