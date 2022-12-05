"""To solve this problem, we need to create a program that will simulate the octopuses' behavior. To do this, we can create a two-dimensional array of integers to represent the grid of octopuses. Then, we can iterate through the array and simulate the behavior of the octopuses in each step.

Here is a possible solution in Python:

"""
# Read the input from the file
with open("11_input") as input_file:
    octopus_grid = [list(map(int, line.strip())) for line in input_file]

# Function to simulate the behavior of the octopuses
def simulate_octopuses(grid):
    # Create a new grid to store the updated energy levels
    new_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    
    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Increase the energy level of each octopus by 1
            new_grid[i][j] = grid[i][j] + 1
            
            # If an octopus has an energy level greater than 9, it flashes and
            # increases the energy level of all adjacent octopuses by 1
            if grid[i][j] > 9:
                new_grid[i-1][j] += 1
                new_grid[i+1][j] += 1
                new_grid[i][j-1] += 1
                new_grid[i][j+1] += 1
                new_grid[i-1][j-1] += 1
                new_grid[i-1][j+1] += 1
                new_grid[i+1][j-1] += 1
                new_grid[i+1][j+1] += 1
                
                # Set the energy level of the octopus that flashed to 0
                new_grid[i][j] = 0
    
    # Return the updated grid
    return new_grid

# Simulate the octopuses' behavior for 10 steps
for _ in range(10):
    octopus_grid = simulate_octopuses(octopus_grid)

# Print the final state of the octopuses
for row in octopus_grid:
    print("".join(map(str, row)))
""""""