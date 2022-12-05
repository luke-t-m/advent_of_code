"""The following is a correct solution to the problem described above, written in Python. Note that this solution assumes that the input data is stored in a file called `2_input` and that the file is located in the same directory as the script.

"""
# Open the input file and read the lines into a list
with open('2_input') as f:
    lines = f.read().strip().split('\n')

# Initialize the counters for IDs with exactly two and three of any letter
two_count = 0
three_count = 0

# Loop through each ID
for line in lines:
    # Initialize dictionaries to track the counts of each letter in the ID
    letter_counts = {}
    has_two = False
    has_three = False
    
    # Loop through each letter in the ID
    for letter in line:
        # If the letter is not in the dictionary, add it with a count of 1
        if letter not in letter_counts:
            letter_counts[letter] = 1
        # Otherwise, increment its count
        else:
            letter_counts[letter] += 1
    
    # Loop through the counts of each letter in the ID
    for count in letter_counts.values():
        # If the count is exactly 2, set the `has_two` flag to True
        if count == 2:
            has_two = True
        # If the count is exactly 3, set the `has_three` flag to True
        elif count == 3:
            has_three = True
        # If either flag is already set, we don't need to continue looping
        # through the counts, so we can break out of the loop
        if has_two and has_three:
            break
    
    # If the ID had exactly two of any letter, increment the `two_count` counter
    if has_two:
        two_count += 1
    # If the ID had exactly three of any letter, increment the `three_count` counter
    if has_three:
        three_count += 1

# Calculate the checksum by multiplying the two and three counts together
checksum = two_count * three_count

# Print the checksum
print(checksum)


# Part Two

# Loop through each ID in the list
for i in range(len(lines)):
    # Loop through each other ID in the list, starting at the next index
    for j in range(i + 1, len(lines)):
        # Initialize a counter for the number of different characters in the IDs
        diff_count = 0
        
        # Loop through each character in the IDs, starting at the first index
        for k in range(len(lines[i])):
            # If the characters at index k in the two IDs are different,
            # increment the `diff_count` counter
            if lines[i][k] != lines[j][k]:
                diff_count += 1
        
        # If the `diff_count` is exactly 1, we have found the two correct box IDs
        if diff_count == 1:
            # Initialize a string to hold the common letters in the IDs
            common_letters = ''
            
            # Loop through each character in the IDs, starting at the first index
            for k in range(len(lines[i])):
                # If"""