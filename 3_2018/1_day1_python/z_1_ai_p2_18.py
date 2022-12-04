"""The problem can be solved as follows:

1. Read the input from the specified file.
2. Create a set to keep track of the current frequency.
3. Iterate over the list of frequency changes and update the current frequency.
4. If the current frequency is already in the set, print it and break the loop.

Here is the code in python:

"""
# Read the input from the file
with open('1_input', 'r') as f:
    data = f.read().strip().split('\n')

# Convert the input to integers
data = [int(x) for x in data]

# Create a set to keep track of the current frequency
seen = set()

# Initialize the current frequency
current_frequency = 0

# Loop over the frequency changes
for change in data:
    # Update the current frequency
    current_frequency += change

    # If the current frequency is already in the set, print it and break the loop
    if current_frequency in seen:
        print(current_frequency)
        break

    # Add the current frequency to the set
    seen.add(current_frequency)
""""""