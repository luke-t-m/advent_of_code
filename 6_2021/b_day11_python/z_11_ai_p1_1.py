"""The task is to simulate the evolution of octopuses' energy levels in a grid. The grid is represented by a list of strings. At each time step, the energy level of each octopus increases by 1. Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.) Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

A solution in Python could be:

"""
# Parse input
grid = []
for line in open("11_input", "r"):
  grid.append([int(x) for x in line.strip()])

# Define grid dimensions
width = len(grid[0])
height = len(grid)

# Define helper function to get octopuses in adjacent cells
def adjacent(x, y):
  for i in range(max(0, x - 1), min(width, x + 2)):
    for j in range(max(0, y - 1), min(height, y + 2)):
      if i == x and j == y:
        continue
      yield i, j

# Define main simulation loop
while True:
  # Increase energy level of each octopus by 1
  for x in range(width):
    for y in range(height):
      grid[x][y] += 1

  # Store octopuses that will flash in this step
  to_flash = []

  # Find octopuses that will flash in this step
  for x in range(width):
    for y in range(height):
      if grid[x][y] > 9:
        to_flash.append((x, y))

  # Flash octopuses that need to flash in this step
  for x, y in to_flash:
    # Increase energy level of adjacent octopuses by 1
    for i, j in adjacent(x, y):
      grid[i][j] += 1

  # Stop if no octopuses will flash
  if not to_flash:
    break

  # Set energy level of flashed octopuses to 0
  for x, y in to_flash:
    grid[x][y] = 0

# Print final state of the grid
for line in grid:
  print("".join(str(x) for x in line))
""""""