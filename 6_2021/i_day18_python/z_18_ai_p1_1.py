"""To solve the given problem, we can iterate over the input list of snailfish numbers and apply the rules of reduction on each element of the list until it can't be reduced further. Below is the code to do that:

"""
# Read the input from the file '18_input'
with open('18_input', 'r') as file:
  snailfish_numbers = file.read().splitlines()

# Define the function to explode a pair
def explode(pair):
  # Find the first regular number to the left and right of the pair
  left = next((i for i in pair[::-1] if isinstance(i, int)), None)
  right = next((i for i in pair if isinstance(i, int)), None)

  # If a regular number exists to the left or right of the pair, add the left and right values of the pair to them, respectively
  if left is not None:
    pair[pair.index(left)] += pair[0]
  if right is not None:
    pair[pair.index(right)] += pair[1]

  # Replace the pair with the regular number 0
  pair[:] = [0]

# Define the function to split a regular number
def split(num):
  # Replace the regular number with a pair where the left value is the regular number divided by two and rounded down,
  # and the right value is the regular number divided by two and rounded up
  num[:] = [num // 2, (num + 1) // 2]

# Iterate over the list of snailfish numbers
for i, snailfish_number in enumerate(snailfish_numbers):
  # Convert the snailfish number to a list
  snailfish_number = [snailfish_number[1:-1].split(",")]

  # Keep reducing the snailfish number until it can't be reduced further
  while True:
    # Check if there are any pairs nested inside four pairs
    nested_pairs = [i for i in snailfish_number if isinstance(i, list) and len([j for j in i if isinstance(j, list)]) >= 4]

    # If there are, explode the leftmost such pair
    if nested_pairs:
      explode(nested_pairs[0])

    # If there are no nested pairs, check if there are any regular numbers that are 10 or greater
    else:
      large_nums = [i for i in snailfish_number if isinstance(i, int) and i >= 10]

      # If there are, split the leftmost such regular number
      if large_nums:
        split(large_nums[0])

      # If there are no nested pairs or large regular numbers, the snailfish number can't be reduced further
      else:
        break

  # Print the reduced snailfish number
  print(snailfish_number)
""""""