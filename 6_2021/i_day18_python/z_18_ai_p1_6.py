"""Here is a solution to the problem:

"""
def reduce_number(number):
  # Recursively reduce each element in the pair
  if isinstance(number, list):
    number = [reduce_number(x) for x in number]

    # Check if any pair is nested inside four pairs
    if any(isinstance(x, list) and len(x) == 2 and all(isinstance(y, list) for y in x) for x in number):
      # Find the leftmost pair that meets the explode criteria
      for i, x in enumerate(number):
        if isinstance(x, list) and len(x) == 2 and all(isinstance(y, list) for y in x):
          # Explode the pair and return the result
          left = 0 if i == 0 else number[i - 1]
          right = 0 if i == len(number) - 1 else number[i + 1]
          number[i] = 0
          return [left + x[0], right + x[1]]

    # Check if any regular number is 10 or greater
    if any(isinstance(x, int) and x >= 10 for x in number):
      # Find the leftmost regular number that meets the split criteria
      for i, x in enumerate(number):
        if isinstance(x, int) and x >= 10:
          # Split the regular number and return the result
          left = x // 2
          right = x - left
          number[i] = [left, right]
          return number

  # Return the reduced number
  return number


def add_numbers(a, b):
  # Add the two numbers together by forming a pair
  result = [a, b]

  # Reduce the result until no actions apply
  while True:
    reduced = reduce_number(result)
    if reduced == result:
      break
    result = reduced

  return result


# Read the input
with open("18_input") as file:
  numbers = [eval(line.strip()) for line in file]

# Add the numbers together and print the result
result = reduce_number(add_numbers(*numbers))
print(result)
"""

To run this code, save it in a file called `solution.py` and run it with the following command:

"""
python solution.py
"""

This code assumes that the input is in the following format, where each line contains a single snailfish number:

"""
[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
"""

The output of this code will be the reduced result of adding the two snailfish numbers. For example, if the input is:

"""
[[1,2],[3,4]]
[[5,6],[7,8]]
"""

The"""