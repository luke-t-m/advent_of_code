"""To solve this problem, we will need to simulate the 100 steps of octopus energy levels and flashing. Here is one way to do that in Python:

"""
# Read the input from the file "11_input"
with open("11_input") as f:
  # Create a 2D list of octopus energy levels
  octopuses = [list(map(int, line.strip())) for line in f]

# Initialize the number of flashes to 0
flashes = 0

# Loop for 100 steps
for _ in range(100):
  # Increase the energy level of each octopus by 1
  for i in range(10):
    for j in range(10):
      octopuses[i][j] += 1
  
  # Create a set to store the coordinates of octopuses that flashed
  flashed = set()

  # Loop over the octopuses again
  for i in range(10):
    for j in range(10):
      # If an octopus has energy level greater than 9,
      # add its coordinates to the set and increase the flash count
      if octopuses[i][j] > 9:
        flashed.add((i, j))
        flashes += 1

  # Loop over the octopuses that flashed
  for i, j in flashed:
    # Set the energy level of the octopus to 0
    octopuses[i][j] = 0
    # Loop over its neighbors (including diagonally adjacent octopuses)
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
      # If the neighbor is inside the grid, increase its energy level by 1
      if 0 <= x < 10 and 0 <= y < 10:
        octopuses[x][y] += 1

# Print the number of flashes
print(flashes)
"""

This code first reads the input from the file "11_input" and stores it in a 2D list called `octopuses`. Then it simulates the 100 steps by increasing the energy level of each octopus by 1 in each step, checking for octopuses with energy level greater than 9, and flashing them. It keeps track of the octopuses that have flashed and their neighbors, and increases the energy level of their neighbors by 1 in the next step. Finally, it prints the number of flashes that occurred in the 100 steps."""