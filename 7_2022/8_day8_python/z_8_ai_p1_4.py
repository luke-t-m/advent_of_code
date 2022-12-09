"""Here is a solution to the problem:

"""
with open('8_input') as f:
    data = f.read()

# Split the input data into a list of rows
rows = data.split('\n')

# Remove the last element if it's empty (it will be if the input ends with a newline)
if rows[-1] == '':
    rows = rows[:-1]

# Count the number of trees in each direction
num_trees = [0, 0, 0, 0]
# The starting position
pos = (0, 0)
# The direction vector for each direction
directions = [(1, 1), (1, 3), (1, 5), (1, 7)]

# Loop over the directions
for i in range(4):
    # Get the direction vector for this direction
    d = directions[i]
    # Set the current position to the starting position
    p = pos
    # Count the number of trees in this direction
    while p[0] < len(rows) and p[1] < len(rows[0]):
        # If this position contains a tree, increment the tree count
        if rows[p[0]][p[1]] == '#':
            num_trees[i] += 1
        # Move to the next position in this direction
        p = (p[0] + d[0], p[1] + d[1])

# Print the total number of trees
print(num_trees[0] * num_trees[1] * num_trees[2] * num_trees[3])
""""""