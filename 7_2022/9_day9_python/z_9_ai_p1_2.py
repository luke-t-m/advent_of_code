"""The following is a correct solution to the problem in python:

"""
# Read input from 9_input file
with open("9_input") as f:
    input_string = f.read()

# Split input_string into a list of individual moves
moves = input_string.split("\n")

# Initialize the position of the head and tail as [0, 0]
head = [0, 0]
tail = [0, 0]

# Iterate through the moves
for move in moves:
    # Get the direction and distance of the move
    direction = move[0]
    distance = int(move[1:])

    # Update the position of the head
    if direction == "U":
        head[1] += distance
    elif direction == "D":
        head[1] -= distance
    elif direction == "L":
        head[0] -= distance
    elif direction == "R":
        head[0] += distance

    # Update the position of the tail if the head and tail are not adjacent
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        if direction == "U":
            tail[1] += 1
        elif direction == "D":
            tail[1] -= 1
        elif direction == "L":
            tail[0] -= 1
        elif direction == "R":
            tail[0] += 1

# Print the final position of the tail
print(tail)
""""""