"""To solve this problem, you will need to read in the frequency changes from the file named `1_input`. Then, you will need to repeatedly apply these frequency changes until you find the first frequency that is reached twice. Here is some sample code in Python that does this:

"""
# open the input file
with open("1_input") as input_file:
  # read in all the frequency changes as a list of integers
  changes = [int(x) for x in input_file.read().split("\n") if x != ""]

# initialize the current frequency to 0
current_frequency = 0

# initialize a set to keep track of the frequencies we've seen
seen_frequencies = set()

# keep looping until we find a frequency that has been seen before
while True:
  # loop through all the frequency changes
  for change in changes:
    # update the current frequency
    current_frequency += change

    # if we've seen this frequency before, print it and exit the loop
    if current_frequency in seen_frequencies:
      print(current_frequency)
      exit()

    # otherwise, add the current frequency to the set of seen frequencies
    seen_frequencies.add(current_frequency)
"""

This code should read in the frequency changes from the input file, apply them repeatedly until it finds the first frequency that is reached twice, and then print the answer."""