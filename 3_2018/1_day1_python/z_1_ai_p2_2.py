"""To solve this problem, we need to find the first frequency that is reached twice after applying a list of frequency changes to the starting frequency of 0.

One way to solve this problem is to use a set to keep track of the frequencies that have been reached so far. We can then iterate through the list of frequency changes, adding each change to the current frequency and checking if the resulting frequency has already been seen. If it has, we can print the frequency and stop the loop. Otherwise, we can add the frequency to the set and continue the loop.

Here is one way to implement this solution in Python:

"""
# Read the list of frequency changes from the input file
with open('1_input') as f:
    changes = [int(x) for x in f.readlines()]

# Set the initial frequency to 0
frequency = 0

# Create a set to store the frequencies that have been reached
frequencies = set()

# Iterate through the list of changes
for change in changes:
    # Update the current frequency
    frequency += change

    # Check if the current frequency has been seen before
    if frequency in frequencies:
        # If it has, print the frequency and stop the loop
        print(frequency)
        break

    # If the frequency has not been seen before, add it to the set
    frequencies.add(frequency)
"""

To run this code, save it to a file called `solution.py` and run it using the following command:

"""
"""

This should print the first frequency that is reached twice to the console."""