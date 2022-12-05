"""To solve this problem, we can keep track of the current frequency as we iterate through the list of frequency changes. If we encounter a frequency that we have already seen, we can print it and stop the program. Here is one way to solve this problem in Python:

"""
# Open the input file and read the list of frequency changes
with open("1_input") as f:
  changes = [int(x) for x in f.read().splitlines()]

# Keep track of the current frequency and the set of frequencies we have seen
current_freq = 0
seen_freqs = {current_freq}

# Iterate through the list of frequency changes
for change in changes:
  # Update the current frequency and add it to the set of seen frequencies
  current_freq += change
  if current_freq in seen_freqs:
    # If we have seen this frequency before, print it and stop the program
    print(current_freq)
    break
  else:
    # If we have not seen this frequency before, add it to the set
    seen_freqs.add(current_freq)

# If we have not found a duplicate frequency, print a message
if current_freq not in seen_freqs:
  print("No duplicate frequency found")
"""

To use this code, you will need to save it to a file (e.g. `1_solution.py`) and run it using Python. The first duplicate frequency that is found will be printed to the console."""