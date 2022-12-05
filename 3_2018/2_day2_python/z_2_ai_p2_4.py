"""To solve this problem, we first need to read the input from the file `2_input`. This can be done using the `open` and `readlines` functions in Python:

"""
with open('2_input', 'r') as f:
    lines = f.readlines()
"""

Next, we need to count the number of box IDs that have exactly two of any letter and the number of IDs that have exactly three of any letter. This can be done by iterating over the list of IDs and using the `count` method to count the number of times a letter appears in each ID:

"""
two_count = 0
three_count = 0

for line in lines:
    # Remove newline character from line
    line = line.strip()

    # Initialize counts for each letter to 0
    counts = [0] * 26

    # Count the number of times each letter appears in the line
    for c in line:
        counts[ord(c) - ord('a')] += 1

    # Check if any letter appears exactly two or three times
    # and update the counts accordingly
    if 2 in counts:
        two_count += 1
    if 3 in counts:
        three_count += 1
"""

Now that we have the counts, we can compute the checksum by multiplying `two_count` and `three_count`:

"""
checksum = two_count * three_count
"""

Finally, to find the box IDs that differ by exactly one character, we need to iterate over all pairs of IDs and compare them character by character. If the IDs differ by exactly one character, we can output the common letters by removing the differing character:

"""
for line1 in lines:
    for line2 in lines:
        # Remove newline characters from lines
        line1 = line1.strip()
        line2 = line2.strip()

        # Count the number of characters that differ
        diff_count = 0
        common_letters = ""
        for c1, c2 in zip(line1, line2):
            if c1 != c2:
                diff_count += 1
            else:
                common_letters += c1

        # If the IDs differ by exactly one character,
        # output the common letters
        if diff_count == 1:
            print(line1, line2)