"""Here is a solution to the problem in Python:

"""
# Read input from file
with open("1_input", "r") as f:
  changes = f.readlines()

# Parse input as integers
changes = [int(x) for x in changes]

# Initialize current frequency
curr_freq = 0

# Initialize set to keep track of frequencies reached
freqs = set()

# Loop until a frequency is reached twice
while curr_freq not in freqs:
  # Add current frequency to set
  freqs.add(curr_freq)
  
  # Update current frequency
  curr_freq += changes.pop(0)

  # If we run out of changes, start again from the beginning
  if not changes:
    changes = [int(x) for x in f.readlines()]

# Print the first frequency reached twice
print(curr_freq)
"""

To run this solution, save it to a file called `1.py` and run it with `python 1.py`. This will print the answer to the problem to the console."""