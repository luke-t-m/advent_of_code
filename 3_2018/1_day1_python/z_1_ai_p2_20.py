"""Here's a solution to the problem in python:

"""
with open('1_input') as f:
  input = f.read().strip().split('\n')

current_frequency = 0
seen_frequencies = set()

while True:
  for change in input:
    current_frequency += int(change)

    if current_frequency in seen_frequencies:
      print(current_frequency)
      exit()
    else:
      seen_frequencies.add(current_frequency)
"""

This code first reads in the input from the file `1_input`, and stores it in a list called `input`. It then initializes a variable `current_frequency` to 0, and a set `seen_frequencies` to keep track of the frequencies we've already seen.

It then enters an infinite loop, which iterates over the changes in the `input` list. For each change, it updates `current_frequency` by adding the change to it. It then checks if the current frequency is in the set of seen frequencies. If it is, it prints the current frequency and exits the program. Otherwise, it adds the current frequency to the set of seen frequencies and continues to the next iteration.

This code should solve the problem as stated and print the first frequency that is reached twice."""