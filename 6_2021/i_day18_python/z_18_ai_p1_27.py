"""The following code solves the problem as described above.

"""
# Helper function to explode a snailfish number
def explode(snailfish):
  # If any pair is nested inside four pairs, the leftmost such pair explodes
  if len(snailfish) == 5:
    left, middle, middle2, middle3, right = snailfish
    left_exploded = explode(left)
    right_exploded = explode(right)
    # The left value is added to the first regular number to the left of the exploding pair (if any)
    if isinstance(left_exploded, int):
      left_exploded += middle[0]
      middle = (0, middle[1])
    # The right value is added to the first regular number to the right of the exploding pair (if any)
    if isinstance(right_exploded, int):
      right_exploded += middle3[1]
      middle3 = (middle3[0], 0)
    return [left_exploded, middle, middle2, middle3, right_exploded]

  # If any regular number is 10 or greater, the leftmost such regular number splits
  if isinstance(snailfish[0], int) and snailfish[0] >= 10:
    num = snailfish[0]
    left = num // 2
    right = (num + 1) // 2
    return [left, right] + snailfish[1:]

  # If no action in the above list applies, the snailfish number is reduced
  return snailfish

# Helper function to reduce a snailfish number
def reduce(snailfish):
  # Repeatedly apply the first action in the list that applies to the snailfish number
  while True:
    exploded = explode(snailfish)
    if exploded == snailfish:
      break
    snailfish = exploded

  # Flatten the reduced snailfish number
  result = []
  for x in snailfish:
    if isinstance(x, list):
      result.extend(x)
    else:
      result.append(x)

  return result

# Function to add two snailfish numbers
def add(a, b):
  # Form a pair from the left and right parameters of the addition operator
  snailfish = [a, b]

  # Reduce the snailfish number
  return reduce(snailfish)

# Read input from file
with open("18_input") as f:
  # Split the input into lines
  lines = f.read().strip().split("\n")

# Process each line of input
for line in lines:
  # Parse the snailfish number from the line of input
  snailfish = eval(line)

  # Add 1 to the snailfish number and print the result
  print(add(snailfish, [1, 1]))
""""""