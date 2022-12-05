"""The following code should solve the problem. It reads the input from a file called 1_input and prints the answer.
"""
# Read the input from the file
with open('1_input') as f:
    changes = f.readlines()

# Parse the input
changes = [int(x) for x in changes]

# Keep track of the current frequency and the frequencies that have been seen
current_frequency = 0
seen_frequencies = set()

# Keep going until we reach a frequency that has been seen before
while current_frequency not in seen_frequencies:
    # Add the current frequency to the set of seen frequencies
    seen_frequencies.add(current_frequency)

    # Update the current frequency
    current_frequency += changes[0]
    changes = changes[1:] + [changes[0]]

# Print the first frequency that was reached twice
print(current_frequency)
""""""