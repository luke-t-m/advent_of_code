"""Here's a simple solution in Python that reads the frequency changes from a file called `1_input`, loops over the list of frequency changes, and keeps track of the current frequency and a set of frequencies that have been seen before. When the current frequency has been seen before, the solution prints the frequency and exits the loop.

"""
# Read the input from the file.
with open("1_input") as file:
    changes = [int(change) for change in file]

# Keep track of the current frequency and the set of frequencies that have been seen.
current_frequency = 0
seen_frequencies = set([current_frequency])

# Loop until we find a frequency that has been seen before.
for change in itertools.cycle(changes):
    current_frequency += change
    if current_frequency in seen_frequencies:
        print(current_frequency)
        break
    seen_frequencies.add(current_frequency)
""""""