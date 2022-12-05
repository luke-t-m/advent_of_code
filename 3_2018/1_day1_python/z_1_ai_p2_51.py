"""You need to write a program that reads a list of integers from a file called `1_input` and outputs the first frequency that is reached twice. Here's how you could do this in Python:

"""
# Read the input from the file
with open("1_input") as f:
    changes = [int(x) for x in f.read().strip().split("\n")]

# Keep track of the current frequency and the frequencies that have been reached
current_frequency = 0
reached_frequencies = set([current_frequency])

# Repeatedly apply the changes
while True:
    for change in changes:
        current_frequency += change

        # Check if the current frequency has been reached before
        if current_frequency in reached_frequencies:
            print(current_frequency)
            exit()

        # Otherwise, add the current frequency to the set of reached frequencies
        reached_frequencies.add(current_frequency)
"""

You can then run this program and it will output the first frequency that is reached twice."""