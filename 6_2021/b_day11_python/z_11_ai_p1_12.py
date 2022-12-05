"""The following python code will solve the problem as described.

"""python
# read input from the file
with open("11_input", "r") as file:
    data = file.read()

# convert the input into a 2D array of integers
octopuses = [[int(char) for char in line] for line in data.strip().split("\n")]

# simulate 100 steps
for i in range(100):
    # increase energy level of all octopuses by 1
    octopuses = [[energy + 1 for energy in row] for row in octopuses]
    
    # find octopuses that have energy level greater than 9
    flashing_octopuses = []
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            if octopuses[i][j] > 9:
                flashing_octopuses.append((i, j))
                
    # increase energy level of adjacent octopuses by 1
    for i, j in flashing_octopuses:
        for x in range(max(0, i - 1), min(i + 2, len(octopuses))):
            for y in range(max(0, j - 1), min(j + 2, len(octopuses[i]))):
                octopuses[x][y] += 1
                
    # set energy level of flashing octopuses to 0
    for i, j in flashing_octopuses:
        octopuses[i][j] = 0

# count the total number of flashes
flashes = len(flashing_octopuses)

# print the answer
print(flashes)
""""""