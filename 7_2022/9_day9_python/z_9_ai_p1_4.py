"""Here is a solution to the problem in Python:

"""
# Read the input
with open("9_input") as f:
  input = f.read().strip()

# Initialize the head and tail positions to be the same
head_row, head_col = tail_row, tail_col = 0, 0

# Split the input into a list of directions
directions = input.split("\n")

# Loop through each direction
for direction in directions:
  # Get the movement direction and the number of steps
  move, steps = direction[0], int(direction[1:])

  # Update the head position
  if move == "U":
    head_row -= steps
  elif move == "D":
    head_row += steps
  elif move == "L":
    head_col -= steps
  elif move == "R":
    head_col += steps

  # Update the tail position
  # If the head and tail are in the same row or column, move the tail in the same direction as the head
  if head_row == tail_row or head_col == tail_col:
    if move == "U":
      tail_row -= steps
    elif move == "D":
      tail_row += steps
    elif move == "L":
      tail_col -= steps
    elif move == "R":
      tail_col += steps
  # If the head and tail are not in the same row or column, move the tail one step diagonally
  else:
    if move == "U":
      tail_row -= 1
    elif move == "D":
      tail_row += 1
    elif move == "L":
      tail_col -= 1
    elif move == "R":
      tail_col += 1

# Print the final tail position
print(tail_row, tail_col)
""""""