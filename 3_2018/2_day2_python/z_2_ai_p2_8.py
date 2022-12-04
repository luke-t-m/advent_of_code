"""To solve this problem, we can first count the number of boxes that contain exactly two or three of any letter. We can do this by using a dictionary to store the counts of each letter in the box ID, then looping through the counts and incrementing the count of two and three if we find a count that matches.

To find the box IDs that differ by exactly one character at the same position, we can compare each ID to every other ID and check if they differ by only one character. If so, we can return the common letters between the two IDs. Here is one way to solve this problem in Python:

"""
# Read in the input from the file
with open('2_input', 'r') as f:
    lines = f.read().strip().split('\n')

# Initialize counts for boxes with exactly two or three of any letter
two = 0
three = 0

# Loop through each box ID
for box in lines:
    # Create a dictionary to store the counts of each letter
    counts = {}

    # Loop through each letter in the box ID
    for letter in box:
        # Increment the count of the letter in the dictionary
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1

    # Check if the box ID contains exactly two or three of any letter
    if 2 in counts.values():
        two += 1
    if 3 in counts.values():
        three += 1

# Calculate and print the checksum (two * three)
print(two * three)

# Loop through each box ID
for i, box1 in enumerate(lines):
    # Compare the current box ID to every other box ID
    for box2 in lines[i+1:]:
        # Initialize a counter for the number of differing characters
        diff = 0

        # Loop through the characters in both IDs and compare them
        for a, b in zip(box1, box2):
            # If the characters are different, increment the counter
            if a != b:
                diff += 1

        # If the IDs differ by only one character, print the common letters
        if diff == 1:
            common = ''.join([a for a, b in zip(box1, box2) if a == b])
            print(common)
"""

This code will read in the input from a file called `2_input`, then calculate and print the checksum, followed by the common letters between the two box IDs that differ by only one character."""