"""The first step in solving this problem is to read the input data from the file `8_input`. This can be done using the `open()` and `readlines()` functions.

"""
with open('8_input') as f:
    data = f.readlines()
"""

Next, we need to parse the input data to create a 2D grid of integers representing the height of each tree. This can be done using a list comprehension and the `strip()` method to remove any leading or trailing whitespace from each line of the input.

"""
grid = [[int(x) for x in line.strip()] for line in data]
"""

Once we have the grid of tree heights, we can iterate over the rows and columns of the grid to count the number of trees that are visible from the outside. To do this, we can use a nested loop to iterate over the rows and columns of the grid, and then use a separate loop to iterate over the elements in the current row or column. We can use the `max()` function to find the tallest tree in the current row or column, and then use an `if` statement to check if the current tree is the tallest. If it is, we can increment a counter variable to keep track of the total number of visible trees.

"""
visible_trees = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        tallest = max(grid[i])
        if grid[i][j] == tallest:
            visible_trees += 1
"""

Once we have counted the number of visible trees in each row, we can repeat the process for each column. To do this, we can transpose the grid using the `zip()` function, and then use the same loop as above to count the number of visible trees in each column.

"""
grid_transposed = zip(*grid)
for i in range(len(grid_transposed)):
    for j in range(len(grid_transposed[0])):
        tallest = max(grid_transposed[i])
        if grid_transposed[i][j] == tallest:
            visible_trees += 1
"""

Finally, we can print the total number of visible trees using the `print()` function.

"""
print(visible_trees)
"""

The complete solution to this problem is shown below.

"""
with open('8_input') as f:
    data = f.readlines()

grid = [[int(x) for x in line.strip()] for line in data]

visible_trees = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        tallest = max(grid[i])
        if grid[i][j] == tallest:
            visible_trees += 1

grid_transposed = zip(*grid)
for i in range(len(grid_transposed)):
    for j in range(len(grid_transposed[0])):
        tallest = max(grid_transposed[i])
        if grid_transposed[i][j] == tallest:
            visible_trees += 1

print(visible_trees)
""""""