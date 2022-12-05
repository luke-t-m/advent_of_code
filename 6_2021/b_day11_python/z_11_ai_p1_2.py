"""The problem can be solved by simulating the evolution of the grid of octopuses. We start by reading the grid from the input file, then we apply the rules described in the problem statement to update the grid. We repeat this process until the grid stops changing, which happens when no octopus flashes anymore. To avoid infinite loops, we limit the number of steps to a maximum value.

Here is one possible implementation in Python:

"""
# Read grid from input file
with open('11_input', 'r') as f:
    grid = [[int(x) for x in line.strip()] for line in f]

# Maximum number of steps
max_steps = 100

# Apply rules to update the grid until it stops changing or we reach the maximum number of steps
for step in range(max_steps):
    # Save the current grid
    prev_grid = grid.copy()

    # Increase energy of all octopuses
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1

    # Check if any octopus flashed
    flashed = False
    for i in range(10):
        for j in range(10):
            # Check if octopus flashed
            if grid[i][j] > 9:
                # Set octopus energy to 0
                grid[i][j] = 0

                # Increase energy of adjacent octopuses
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        grid[ni][nj] += 1

                # Octopus flashed
                flashed = True

    # Stop if no octopus flashed
    if not flashed:
        break

# Print the final grid
for row in grid:
    print(''.join(str(x) for x in row))
"""

The final grid will be printed to the standard output."""