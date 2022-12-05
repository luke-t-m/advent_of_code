"""The solution to this problem involves simulating the steps described in the problem statement. We can do this by representing the grid of octopuses as a two-dimensional array, where each element of the array represents the energy level of a single octopus.

First, we can initialize the array by reading the input from the file `11_input`. We can then iterate over the array, and update the energy levels of each octopus according to the rules in the problem statement. After each step, we can count the number of octopuses that have flashed, and add this to a running total.

Here is some sample code that solves the problem:

"""
# Read input from the file
with open('11_input') as f:
  # Initialize the grid of octopuses
  grid = [list(map(int, line.strip())) for line in f]

# The number of steps to simulate
steps = 100

# The total number of flashes
total_flashes = 0

# Simulate the steps
for i in range(steps):
  # Keep track of which octopuses have flashed
  flashed = set()

  # Increase the energy level of each octopus
  for y in range(10):
    for x in range(10):
      grid[y][x] += 1

  # Find octopuses that have flashed
  for y in range(10):
    for x in range(10):
      if grid[y][x] >= 10:
        flashed.add((x, y))

  # Increase the energy level of adjacent octopuses
  for x, y in flashed:
    for dx in [-1, 0, 1]:
      for dy in [-1, 0, 1]:
        # Check if the coordinates are valid
        if 0 <= x + dx < 10 and 0 <= y + dy < 10:
          # Increase the energy level of the adjacent octopus
          grid[y + dy][x + dx] += 1

  # Reset the energy level of octopuses that have flashed
  for x, y in flashed:
    grid[y][x] = 0

  # Add the number of flashes to the total
  total_flashes += len(flashed)

# Print the total number of flashes
print(total_flashes)
""""""