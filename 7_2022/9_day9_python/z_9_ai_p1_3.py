"""The problem statement describes the following rules for moving the tail:
- If the head is two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough.
- Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up.

We can implement these rules in a function that takes the current positions of the head and the tail and returns the updated position of the tail. Here is one way to do it:

"""
def move_tail(head, tail):
    # If the head is two steps directly up, down, left, or right from the tail,
    # the tail must also move one step in that direction so it remains close enough.
    if (head[0] == tail[0] and abs(head[1] - tail[1]) == 2) or \
       (head[1] == tail[1] and abs(head[0] - tail[0]) == 2):
        return (tail[0] + (head[0] - tail[0]) // 2, tail[1] + (head[1] - tail[1]) // 2)

    # Otherwise, if the head and tail aren't touching and aren't in the same row or column,
    # the tail always moves one step diagonally to keep up.
    if head[0] != tail[0] and head[1] != tail[1]:
        return (tail[0] + (head[0] - tail[0]) // abs(head[0] - tail[0]),
                tail[1] + (head[1] - tail[1]) // abs(head[1] - tail[1]))

    # If the head and tail are already touching, the tail doesn't move.
    return tail
"""

Next, we need to read the series of motions from the input file and apply them to the head and tail. We can do that like this:

"""
# Read the input file.
with open("9_input") as file:
    moves = file.read().strip().split("\n")

# Initialize the head and tail at the same position.
head = (0, 0)
tail = (0, 0)

# Apply each move in the series of moves to the head and tail.
for move in moves:
    direction = move[0]
    distance = int(move[1:])

    # Update the position of the head.
    if direction == "U":
        head = (head[0] - distance, head[1])
    elif direction == "D":
        head = (head[0] + distance, head[1])
    elif direction == "L":
        head = (head[0], head[1] - distance)
    elif direction == "R":
        head = (head[0], head[1] + distance)

    # Update the position of the tail.
    tail = move_tail(head, tail)

# Print the final position of the tail.
print(tail)
"""

Here is the complete code:

"""
def move_tail(head, tail):
    # If the head is two steps directly up, down, left, or right from the tail,
    # the tail must also move one step in"""