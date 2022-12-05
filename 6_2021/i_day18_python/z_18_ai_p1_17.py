"""To solve this problem, we will use a recursive function that applies the reduction rules in a loop until the number is reduced. The function will take a snailfish number as input and return the reduced number as output.

First, we define a function `is_pair` that checks if a given value is a pair. We can do this by checking if the value is a list with two elements.

Next, we define the `reduce_number` function. This function takes a snailfish number as input and applies the reduction rules in a loop until the number is reduced. If any pair is nested inside four pairs, we explode the leftmost such pair by adding its left and right values to the first regular number to the left and right of the pair, respectively. If any regular number is 10 or greater, we split the leftmost such number by replacing it with a pair whose left and right values are the regular number divided by two and rounded down and up, respectively.

Once no action in the above list applies, the snailfish number is reduced and the function returns the reduced number.

Here is the code:

"""
def is_pair(val):
  return isinstance(val, list) and len(val) == 2

def reduce_number(num):
  # If the number is a pair nested inside four pairs, explode it
  if is_pair(num) and is_pair(num[0]) and is_pair(num[0][0]) and is_pair(num[0][0][0]):
    # Add the left and right values of the pair to the first regular number to the left and right of the pair, respectively
    left_num = num[0][0][0][0]
    right_num = num[0][0][0][1]
    num[0][0][0] = 0
    if left_num >= 10:
      num[0][0][0] = [left_num // 2, (left_num + 1) // 2]
    if right_num >= 10:
      num[0][0][1] = [right_num // 2, (right_num + 1) // 2]
    return reduce_number(num)
  # If the number contains a regular number >= 10, split it
  elif isinstance(num, list):
    for i in range(len(num)):
      if isinstance(num[i], int) and num[i] >= 10:
        num[i] = [num[i] // 2, (num[i] + 1) // 2]
        return reduce_number(num)
  # Otherwise, the number is reduced and we return it
  return num

# Read the input from the file "18_input"
with open("18_input") as f:
  input_lines = f.readlines()

# Parse the input and compute the sum of the snailfish numbers
sum = [0, 0]
for line in input_lines:
  num = eval(line.strip())
  sum = reduce_number(sum + num)

# Print the reduced result
print(sum)
""""""