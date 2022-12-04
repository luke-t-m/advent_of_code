"""To solve this problem, we need to read the input from a file called 2_input. We can do this using the `open` function, which returns a file object that we can read from. Then, we can iterate over the lines in the file and keep track of the number of IDs that have exactly two or three of any letter. We can then multiply these counts together to get the checksum.

Here is one way to implement this in Python:

"""
# Open the input file and read the lines
with open('2_input') as f:
    lines = f.readlines()

# Initialize counters for IDs with exactly two and three of any letter
two_count = 0
three_count = 0

# Iterate over the lines in the file
for line in lines:
    # Initialize a dictionary to keep track of the frequency of each letter
    counts = {}

    # Iterate over the letters in the line
    for c in line:
        # If the letter is not in the dictionary, add it with a count of 1
        if c not in counts:
            counts[c] = 1
        # Otherwise, increment the count for that letter
        else:
            counts[c] += 1

    # Initialize flags for whether the ID has exactly two and three of any letter
    has_two = False
    has_three = False

    # Iterate over the counts in the dictionary
    for count in counts.values():
        # If the ID has exactly two of any letter and we haven't already counted it, increment the counter
        if count == 2 and not has_two:
            two_count += 1
            has_two = True

        # If the ID has exactly three of any letter and we haven't already counted it, increment the counter
        elif count == 3 and not has_three:
            three_count += 1
            has_three = True

        # If the ID has both two and three of any letter, we can stop iterating
        if has_two and has_three:
            break

# Print the checksum, which is the product of the number of IDs with exactly two and three of any letter
print(two_count * three_count)
""""""