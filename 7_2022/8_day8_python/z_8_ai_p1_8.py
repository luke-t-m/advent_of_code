"""The task is to count the number of trees that are visible from outside the grid when looking directly along a row or column.

First, we need to read the input from the file `8_input`.

Next, we need to parse the input to extract the grid of tree heights.

Then, we need to iterate over each row and column of the grid, and for each element, we need to count the number of trees that are visible from that element in the four directions (up, down, left, and right).

To do this, we need to check if the current element is the tallest in its row or column. If it is, we increment the counter by 1.

Finally, we print the total number of visible trees.

Here is one possible solution:

"""
with open('8_input') as f:
    grid = [list(map(int, line.strip())) for line in f]

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        # Check if the current element is the tallest in its row
        if grid[i][j] == max(grid[i]):
            count += 1

        # Check if the current element is the tallest in its column
        if grid[i][j] == max([grid[x][j] for x in range(len(grid))]):
            count += 1

print(count)
""""""