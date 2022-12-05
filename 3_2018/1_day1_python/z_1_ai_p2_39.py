"""To solve this problem, you will need to keep track of the current frequency as you loop over the list of changes. You can do this by using a variable named `current_frequency` initialized to 0. Then, for each change in the list, you can add or subtract the change to `current_frequency`, depending on whether the change is positive or negative.

To find the first frequency that is reached twice, you will need to keep track of the frequencies that have been reached so far in a set. Then, for each change in the list, you can add or subtract the change to `current_frequency`, and check if the resulting frequency is in the set of reached frequencies. If it is, you can print the frequency and stop the loop. Otherwise, you can add the frequency to the set of reached frequencies.

Here is a solution in Python:

"""
# Read the list of changes from the input file
with open('1_input') as f:
    changes = [int(x) for x in f]

# Initialize the current frequency and the set of reached frequencies
current_frequency = 0
reached_frequencies = set([current_frequency])

# Loop over the changes
for change in changes:
    # Update the current frequency
    current_frequency += change

    # If the current frequency has been reached before, print it and stop the loop
    if current_frequency in reached_frequencies:
        print(current_frequency)
        break

    # Otherwise, add the current frequency to the set of reached frequencies
    reached_frequencies.add(current_frequency)
""""""