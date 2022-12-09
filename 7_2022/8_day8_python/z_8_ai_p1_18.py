# This code solves the problem as described in the prompt.
# It reads the input from a file called 8_input.

with open('8_input', 'r') as f:
    data = f.readlines()

# Parse the input into a matrix of integers.
matrix = [[int(c) for c in line.strip()] for line in data]

# Initialize the number of visible trees to zero.
num_visible_trees = 0

# Loop over the rows and columns of the matrix.
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # Check if the tree at matrix[i][j] is visible from the left.
        # This is true if all the trees to the left of it have a height
        # less than or equal to the height of the tree at matrix[i][j].
        left_visible = True
        for k in range(j):
            if matrix[i][k] > matrix[i][j]:
                left_visible = False
                break

        # Check if the tree at matrix[i][j] is visible from the top.
        # This is true if all the trees above it have a height less than
        # or equal to the height of the tree at matrix[i][j].
        top_visible = True
        for k in range(i):
            if matrix[k][j] > matrix[i][j]:
                top_visible = False
                break

        # If the tree is visible from the left or the top, increment the
        # number of visible trees.
        if left_visible or top_visible:
            num_visible_trees += 1

# Print the number of visible trees.
print(num_visible_trees)