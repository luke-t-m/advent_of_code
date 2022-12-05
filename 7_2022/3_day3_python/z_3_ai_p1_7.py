"""To solve this problem, we need to read the contents of the input file, `3_input`, and then process the contents of each rucksack.

First, we can open the input file and read the contents. We can store the contents of the file in a list of strings, where each string represents the contents of a rucksack.

Next, we can iterate over the list of rucksacks and process each one. For each rucksack, we can find the item type that appears in both compartments by creating a set of the characters in the first compartment, and then finding the intersection of that set with the set of characters in the second compartment. The intersection of the two sets will contain the item type that appears in both compartments.

Once we have found the item type that appears in both compartments, we can convert it to a priority by mapping lowercase characters to priorities 1 through 26 and uppercase characters to priorities 27 through 52. We can then add the priority to a running total.

Finally, we can print the sum of the priorities of the item types that appear in both compartments of each rucksack.

Here is an implementation of this solution in Python:

"""
# Open the input file and read the contents
with open('3_input') as file:
    rucksacks = file.readlines()

# Initialize the sum of priorities to 0
sum_of_priorities = 0

# Iterate over the list of rucksacks
for rucksack in rucksacks:
    # Find the item type that appears in both compartments
    # by creating a set of the characters in the first compartment
    # and then finding the intersection of that set with the set
    # of characters in the second compartment
    common_item_type = set(rucksack[:len(rucksack)//2]).intersection(set(rucksack[len(rucksack)//2:]))

    # Convert the common item type to a priority by mapping
    # lowercase characters to priorities 1 through 26 and
    # uppercase characters to priorities 27 through 52
    priority = ord(common_item_type) - ord('a') + 1 if ord(common_item_type) < 80 else ord(common_item_type) - ord('A') + 27

    # Add the priority to the running total
    sum_of_priorities += priority

# Print the sum of the priorities
print(sum_of_priorities)
"""

This solution should produce the correct result when run on the input provided in the problem statement."""