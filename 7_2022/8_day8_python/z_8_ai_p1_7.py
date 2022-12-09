"""# `8_input` should contain the grid of trees.
# This code assumes the file has been correctly formatted,
# with each row of trees on a separate line.
with open('8_input') as f:
    rows = [line.strip() for line in f]

# initialize our count of visible trees to the number of trees on the edges of the grid
num_visible = len(rows) + len(rows[0]) - 2

# for each row and column, find the tallest tree
for i in range(len(rows)):
    # find the tallest tree in this row
    tallest_in_row = max([int(tree) for tree in rows[i]])

    # if the tallest tree in this row is also the tallest tree we've seen so far,
    # increment our count of visible trees
    if tallest_in_row > tallest_so_far:
        tallest_so_far = tallest_in_row
        num_visible += 1

    # repeat the process for columns
    column = [int(rows[j][i]) for j in range(len(rows))]
    tallest_in_col = max(column)
    if tallest_in_col > tallest_so_far:
        tallest_so_far = tallest_in_col
        num_visible += 1

# print the total number of visible trees
print(num_visible)"""