"""First, we need to read the input from the file named 8_input. We can use the `open` function to open the file in read mode and then read the contents using the `readlines` method, which will return a list of strings, where each string is a line from the file.

Next, we can loop through each line of the input and count the number of trees that are visible from outside the grid. To do this, we can loop through each digit in the line, and check if it is the largest digit in that line. If it is, we increment our counter by 1. Finally, we can print the total number of trees that are visible from outside the grid.

Here is the complete solution:

"""
# Open the input file in read mode
with open('8_input', 'r') as f:
    # Read the contents of the file
    lines = f.readlines()

# Initialize a counter for the number of visible trees
visible_trees = 0

# Loop through each line of the input
for line in lines:
    # Loop through each digit in the line
    for i, digit in enumerate(line):
        # Check if the current digit is the largest in the line
        if all(digit > d for d in line[:i] + line[i+1:]):
            # Increment the counter if it is
            visible_trees += 1

# Print the total number of visible trees
print(visible_trees)
""""""