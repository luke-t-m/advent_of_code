"""First, let's read the input from the file `1_input`.

"""
with open("1_input", "r") as f:
    changes = [int(x) for x in f.readlines()]
"""

Now, let's iterate over the `changes` list and keep track of the current frequency. We will use a set to keep track of the frequencies that have been seen so far. If a frequency is repeated, we can stop the iteration and print the result.

"""
current_frequency = 0
seen_frequencies = set()

for change in changes:
    current_frequency += change
    if current_frequency in seen_frequencies:
        print(current_frequency)
        break
    seen_frequencies.add(current_frequency)
"""

This should solve the problem."""