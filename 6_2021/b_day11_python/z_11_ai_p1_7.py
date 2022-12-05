"""Here is the correct solution in Python without comments:

"""
def read_input():
    with open("11_input") as file:
        return [[int(c) for c in line.strip()] for line in file]

def simulate(grid):
    new_grid = [[0] * 10 for _ in range(10)]
    flashes = []
    for i in range(10):
        for j in range(10):
            new_grid[i][j] = grid[i][j] + 1
            if new_grid[i][j] > 9:
                flashes.append((i, j))
    for i, j in flashes:
        new_grid[i][j] = 0
        for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= a < 10 and 0 <= b < 10:
                new_grid[a][b] += 1
    return new_grid

def print_grid(grid):
    for row in grid:
        print("".join(str(cell) for cell in row))

grid = read_input()
for i in range(7):
    grid = simulate(grid)
    print("After step " + str(i + 1) + ":")
    print_grid(grid)
"""

This code reads the input from a file called "11_input" and simulates the flashing of the octopuses for seven steps. It then prints the final state of the grid."""