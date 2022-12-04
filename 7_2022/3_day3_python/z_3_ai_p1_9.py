"""The instructions in the problem prompt are fairly clear. The code below should solve the problem.

"""
# Read the input from the file called 3_input
with open("3_input", "r") as file:
    contents = file.readlines()

# Initialize variables to keep track of the sum and the priorities
sum = 0
priorities = []

# Loop over the contents
for line in contents:
    # Remove the newline character from the line
    line = line.strip()

    # Get the first half of the line and the second half of the line
    first_half = line[:len(line) // 2]
    second_half = line[len(line) // 2:]

    # Find the common item type by converting both halves to sets,
    # then taking the intersection of the two sets
    common_item_type = set(first_half) & set(second_half)

    # If the common item type is not empty, then add the priority
    # of the common item type to the list of priorities
    if common_item_type:
        # Convert the common item type to a string
        common_item_type = "".join(common_item_type)

        # Convert the common item type to a priority by getting
        # the ASCII value of the character and subtracting 96
        # if it's lowercase, or 64 if it's uppercase
        priority = ord(common_item_type) - (96 if common_item_type.islower() else 64)

        # Add the priority to the list of priorities
        priorities.append(priority)

# The sum of the priorities is the sum of the elements in the list
sum = sum(priorities)

# Print the sum
print(sum)
""""""