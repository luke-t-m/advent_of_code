"""You will need to create a file called `2_input` with your input data. Then you can use the following code to solve the problem:

"""
# Read input data
with open('2_input', 'r') as f:
  data = f.read().splitlines()

# Initialize counters for number of boxes with exactly two and three of any letter
two_count = 0
three_count = 0

# Loop over box IDs
for box_id in data:
  # Initialize dictionary to count occurrences of each letter
  counts = {}
  for letter in box_id:
    if letter in counts:
      counts[letter] += 1
    else:
      counts[letter] = 1

  # Check if any letter occurs exactly two or three times
  if 2 in counts.values():
    two_count += 1
  if 3 in counts.values():
    three_count += 1

# Compute and print checksum
checksum = two_count * three_count
print(checksum)
"""

You can run the code by running `python filename.py`, where `filename.py` is the name of the file containing the code. In this case, the code should be saved in a file called `filename.py`."""