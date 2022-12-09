"""First, we need to read the input from the file called 8_input. We can use the `open` function to do this.

We will also need to use the `split` method to split the input into individual rows. We can split on the newline character `\n`.

Then, we need to loop through each row and each column to count the number of visible trees. We can do this using two nested `for` loops.

In the inner loop, we will need to find the maximum height of the trees in that column or row. We can do this using the `max` function.

If the current tree has a height that is equal to the maximum height, we can increment a counter variable to keep track of the number of visible trees.

Finally, we can print the value of the counter variable to get the answer to the problem.

Here is the complete solution:

"""
with open('8_test') as f:
    input = f.read().strip()

rows = input.split('\n')

# Keep track of the number of visible trees
count = 0
print(len(rows))
print(len(rows[0]))
# Loop through each row and each column
for i in range(len(rows)):
    for j in range(len(rows[i])):
        if i == 0 or i == len(rows) -1 or j == 0 or j == len(rows[i]) - 1:
            count += 1
            continue
        # Find the maximum height of the trees in this row or column
        max_height = max([int(rows[x][j]) for x in range(len(rows)) if x ]

        # If the current tree has the maximum height, increment the counter
        if int(rows[i][j]) == max_height:
            count += 1

# Print the answer
print(count) # + 2 * len(rows) + 2 * (len(rows[0]) - 2))
""""""