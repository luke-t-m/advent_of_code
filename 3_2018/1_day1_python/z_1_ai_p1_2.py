"""The following solution can be used to solve the problem.

"""
# Read input from file
with open("1_input") as f:
    input_data = f.readlines()

# Remove newline characters from the end of each line
input_data = [x.strip() for x in input_data]

# Convert the strings in the list to integers
input_data = [int(x) for x in input_data]

# Sum the elements in the list to find the result
result = sum(input_data)

# Print the result
print(result)
""""""