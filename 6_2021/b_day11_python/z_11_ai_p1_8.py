"""The following code will solve the problem by simulating the steps described in the prompt. It reads the initial energy levels from a file called `11_input` and outputs the answer to the console.

"""
# Read initial energy levels from input file
with open('11_input', 'r') as f:
  octopuses = [[int(x) for x in line.strip()] for line in f.readlines()]

# Function to simulate a single step of the process
def simulate_step(octopuses):
  # Increase energy level of each octopus by 1
  for i in range(len(octopuses)):
    for j in range(len(octopuses[i])):
      octopuses[i][j] += 1

  # Flash and increase energy level of adjacent octopuses
  flashes = 0
  for i in range(len(octopuses)):
    for j in range(len(octopuses[i])):
      if octopuses[i][j] > 9:
        flashes += 1
        octopuses[i][j] = 0
        # Check and increase energy level of adjacent octopuses
        for x in [-1, 0, 1]:
          for y in [-1, 0, 1]:
            if x == 0 and y == 0:
              continue
            if 0 <= i + x < len(octopuses) and 0 <= j + y < len(octopuses[i]):
              octopuses[i + x][j + y] += 1

  return flashes

# Simulate 100 steps
total_flashes = 0
for i in range(100):
  total_flashes += simulate_step(octopuses)

# Print the number of flashes after 100 steps
print(total_flashes)
""""""