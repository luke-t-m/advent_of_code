"""To solve this problem, we can keep track of the current frequency as we iterate through the list of changes. We can use a `set` to keep track of the frequencies we've seen so far, and return the first frequency that appears twice.

Here's one way we could do that in Python:

"""
# Read the input from the file
with open("1_input") as f:
    changes = [int(line) for line in f]

# Keep track of the current frequency and the frequencies we've seen so far
current_frequency = 0
seen_frequencies = {0}

# Iterate through the list of changes, updating the current frequency
# and checking if we've seen it before
for change in changes:
    current_frequency += change
    if current_frequency in seen_frequencies:
        print(current_frequency)
        break
    seen_frequencies.add(current_frequency)
"""

We can make this code a bit more concise by using a `while` loop to iterate through the changes until we find a repeated frequency:

"""
# Read the input from the file
with open("1_input") as f:
    changes = [int(line) for line in f]

# Keep track of the current frequency and the frequencies we've seen so far
current_frequency = 0
seen_frequencies = {0}

# Keep iterating through the changes until we find a repeated frequency
i = 0
while True:
    current_frequency += changes[i]
    if current_frequency in seen_frequencies:
        print(current_frequency)
        break
    seen_frequencies.add(current_frequency)
    i = (i + 1) % len(changes)
"""

This code reads the input from a file called `1_input`, keeps track of the current frequency and the frequencies we've seen so far, and prints the first frequency that appears twice."""