"""To solve this problem, we need to read the input from a file called `3_input`, which contains the list of items in each rucksack.

Then, we need to go through each line in the file and find the common item between the two compartments of each rucksack. We can do this by creating two sets containing the items in each compartment and then taking the intersection of these two sets. The common item will be the only element in this intersection.

Once we have found the common item for each rucksack, we need to convert it to its priority. We can do this by checking if the item is uppercase or lowercase and then adding the corresponding number to its ASCII value. For example, if the common item is `a`, its priority will be `ord('a') + 1 = 97 + 1 = 98`.

Finally, we need to find the common item between the three rucksacks of each group. We can do this by creating a set containing the common items of each rucksack and then taking the intersection of these sets. The common item between the three rucksacks will be the only element in this intersection.

Here is an example solution in Python:

"""
# Open the input file and read the lines
with open('3_input') as f:
    lines = f.readlines()

# Go through each line in the input file
for line in lines:
    # Split the line into two compartments
    comp1, comp2 = line[:len(line) // 2], line[len(line) // 2:]

    # Create two sets containing the items in each compartment
    set1, set2 = set(comp1), set(comp2)

    # Take the intersection of the two sets to find the common item
    common_item = set1.intersection(set2)

    # Convert the common item to its priority
    priority = ord(common_item) + 1
    if common_item.isupper():
        priority += 26

    # Print the priority of the common item
    print(priority)

# Create a list of sets containing the common items of each rucksack
common_items = [set1.intersection(set2) for set1, set2 in zip(lines[::2], lines[1::2])]

# Take the intersection of the sets to find the common item between the three rucksacks
badge = common_items[0].intersection(common_items[1], common_items[2])

# Convert the badge to its priority
priority = ord(badge) + 1
if badge.isupper():
    priority += 26

# Print the priority of the badge
print(priority)
""""""