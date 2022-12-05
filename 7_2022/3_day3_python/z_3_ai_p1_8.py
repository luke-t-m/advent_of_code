"""The first thing we need to do is read in the data from the file. We can use the `open()` and `readlines()` functions for this.

"""
with open('3_input') as f:
    data = f.readlines()
"""

Next, we need to process the data to find the item type that appears in both compartments of each rucksack. We can do this by looping through each line in the data, splitting it into two compartments, and then comparing the two compartments to find the common item type.

We can use the `split()` method to split each line into two compartments, and then use the `set()` function to convert each compartment into a set of unique items. We can then use the `intersection()` method to find the items that appear in both compartments.

"""
for line in data:
    comp1, comp2 = line.split()
    comp1 = set(comp1)
    comp2 = set(comp2)
    common_items = comp1.intersection(comp2)
"""

Next, we need to find the priority of each common item. We can do this by looping through the items in the `common_items` set, and using an `if` statement to determine whether the item is uppercase or lowercase. If the item is uppercase, we can add 26 to the ASCII value of the character to find its priority. If the item is lowercase, we can add 1 to the ASCII value of the character to find its priority.

"""
for item in common_items:
    if item.isupper():
        priority = ord(item) + 26
    else:
        priority = ord(item) + 1
"""

Finally, we need to keep track of the sum of the priorities of all common items, and print the result.

"""
total_priority = 0
for line in data:
    comp1, comp2 = line.split()
    comp1 = set(comp1)
    comp2 = set(comp2)
    common_items = comp1.intersection(comp2)
    for item in common_items:
        if item.isupper():
            priority = ord(item) + 26
        else:
            priority = ord(item) + 1
        total_priority += priority

print(total_priority)
"""

We can put all of this together into a single program:

"""
with open('3_input') as f:
    data = f.readlines()

total_priority = 0
for line in data:
    comp1, comp2 = line.split()
    comp1 = set(comp1)
    comp2 = set(comp2)
    common_items = comp1.intersection(comp2)
    for item in common_items:
        if item.isupper():
            priority = ord(item) + 26
        else:
            priority = ord(item) + 1
        total_priority += priority

print(total_priority)
"""

To find the common item type that is carried by all three Elves in each group, we can use a similar approach. We can split each line into two compartments, convert the compartments into sets, and then find the intersection of the three compartments.

"""
for i in range(0, len(data),"""