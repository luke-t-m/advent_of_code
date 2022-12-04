"""The solution to this problem is as follows:

1. Read the input from the file "3_input"
2. Split each line of input into two parts, representing the contents of the two compartments of each rucksack
3. For each rucksack, find the common item type that appears in both compartments
4. Convert each common item type to a priority, where lowercase letters have priorities 1 through 26 and uppercase letters have priorities 27 through 52
5. Sum the priorities of all common item types and print the result

Here is an implementation of this solution in Python:

"""
# Read the input from the file "3_input"
with open("3_input") as f:
    lines = f.readlines()

# Split each line into two parts, representing the contents of the two compartments of each rucksack
lines = [line[:len(line)//2], line[len(line)//2:] for line in lines]

# For each rucksack, find the common item type that appears in both compartments
common_item_types = []
for line in lines:
    # Find all unique item types in each compartment
    comp_1_items = set(line[0])
    comp_2_items = set(line[1])
    # Find the item types that appear in both compartments
    common_items = comp_1_items.intersection(comp_2_items)
    # Since there is only one item type that appears in both compartments, take the first one
    common_item_types.append(common_items[0])

# Convert each common item type to a priority, where lowercase letters have priorities 1 through 26 and uppercase letters have priorities 27 through 52
priorities = []
for item_type in common_item_types:
    if item_type.islower():
        # Lowercase letters have priorities 1 through 26
        priorities.append(ord(item_type) - ord("a") + 1)
    else:
        # Uppercase letters have priorities 27 through 52
        priorities.append(ord(item_type) - ord("A") + 27)

# Sum the priorities of all common item types
total_priority = sum(priorities)

# Print the result
print(total_priority)
""""""