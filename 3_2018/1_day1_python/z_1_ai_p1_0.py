"""To solve this problem, we will read the input from the file named `1_input`, and then apply each change to the current frequency, starting with a frequency of 0. We can then print the resulting frequency after all of the changes have been applied.

Here is some sample code that does this:

"""
# Read the input from the file
with open("1_input") as f:
    changes = [int(x) for x in f.read().split("\n") if x != ""]

# Start with a frequency of 0
current_frequency = 0

# Apply each change to the current frequency
for change in changes:
    current_frequency += change

# Print the resulting frequency
print(current_frequency)
"""

This code reads the input from the file, parses the input as a list of integers, and then applies each change to the current frequency. It then prints the resulting frequency after all of the changes have been applied."""