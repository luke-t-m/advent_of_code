"""The following code reads the input from `8_input` and counts the number of trees that are visible from outside the grid when looking directly along a row or column.

"""
with open('8_input', 'r') as f:
    # Read the input
    data = f.read().strip().split('\n')

# Parse the input into a matrix of integers
grid = [[int(ch) for ch in row] for row in data]

# Count the number of visible trees
n_visible_trees = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        # Check if the current tree is taller than all the trees in its row
        # and column
        is_visible = (
            all(grid[i][k] <= grid[i][j] for k in range(len(grid[i]))) and
            all(grid[k][j] <= grid[i][j] for k in range(len(grid)))
        )
        if is_visible:
            n_visible_trees += 1

# Print the answer
print(n_visible_trees)
""""""