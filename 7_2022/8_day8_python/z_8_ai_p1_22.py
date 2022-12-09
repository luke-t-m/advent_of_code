"""The code below solves the problem.

"""
# Read the input
with open("8_input") as f:
    lines = f.readlines()

# Parse the input
grid = [list(map(int, line.strip())) for line in lines]

# The number of trees visible from the outside
n_visible = 0

# For each edge, we count how many trees are visible from that edge
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            continue

        # Check if the tree is visible from the left edge
        is_visible_from_left = True
        for k in range(j):
            if grid[i][k] > grid[i][j]:
                is_visible_from_left = False
                break
        if is_visible_from_left:
            n_visible += 1

        # Check if the tree is visible from the right edge
        is_visible_from_right = True
        for k in range(j+1, len(grid[i])):
            if grid[i][k] > grid[i][j]:
                is_visible_from_right = False
                break
        if is_visible_from_right:
            n_visible += 1

        # Check if the tree is visible from the top edge
        is_visible_from_top = True
        for k in range(i):
            if grid[k][j] > grid[i][j]:
                is_visible_from_top = False
                break
        if is_visible_from_top:
            n_visible += 1

        # Check if the tree is visible from the bottom edge
        is_visible_from_bottom = True
        for k in range(i+1, len(grid)):
            if grid[k][j] > grid[i][j]:
                is_visible_from_bottom = False
                break
        if is_visible_from_bottom:
            n_visible += 1

# Print the result
print(n_visible)
"""

To run the code, save it to a file (e.g. `main.py`) and run `python main.py`. This will print the number of trees visible from the outside of the grid."""