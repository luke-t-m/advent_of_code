"""Here's a solution that uses a `while` loop to simulate the simulation steps, and a `set` to keep track of which octopuses flashed on the current step:

"""
with open("11_input") as f:
    # Read the starting energy levels from the input file
    energy_levels = [[int(x) for x in line.strip()] for line in f]

# Set the number of simulation steps
num_steps = 100

# Keep track of how many flashes there were
num_flashes = 0

for step in range(num_steps):
    # Set of octopuses that flashed on the current step
    flashed_octopuses = set()

    # Increase the energy level of each octopus by 1
    for i in range(len(energy_levels)):
        for j in range(len(energy_levels[i])):
            energy_levels[i][j] += 1

    # Check which octopuses have an energy level greater than 9
    for i in range(len(energy_levels)):
        for j in range(len(energy_levels[i])):
            if energy_levels[i][j] > 9:
                # If an octopus has an energy level greater than 9,
                # add it to the set of flashed octopuses
                flashed_octopuses.add((i, j))

    # Increase the energy level of each adjacent octopus by 1
    for i, j in flashed_octopuses:
        # Check the octopus to the left
        if j > 0:
            energy_levels[i][j - 1] += 1
        # Check the octopus to the right
        if j < len(energy_levels[i]) - 1:
            energy_levels[i][j + 1] += 1
        # Check the octopus above
        if i > 0:
            energy_levels[i - 1][j] += 1
        # Check the octopus below
        if i < len(energy_levels) - 1:
            energy_levels[i + 1][j] += 1
        # Check the octopus to the top-left
        if i > 0 and j > 0:
            energy_levels[i - 1][j - 1] += 1
        # Check the octopus to the top-right
        if i > 0 and j < len(energy_levels[i]) - 1:
            energy_levels[i - 1][j + 1] += 1
        # Check the octopus to the bottom-left
        if i < len(energy_levels) - 1 and j > 0:
            energy_levels[i + 1][j - 1] += 1
        # Check the octopus to the bottom-right
        if i < len(energy_levels) - 1 and j < len(energy_levels[i]) - 1:
            energy_levels[i + 1][j + 1] += 1

    # Set the energy level of each flashed octopus to 0
    for i, j in flashed_octopuses:
        energy_levels[i][j] = 0

    # Increment the number of flashes
    num_flashes += len(flashed_octopuses)

# Print the number of flashes after 100 steps
print(num_flashes)
"""

This code should work as expected, but it can be made more concise and efficient by"""