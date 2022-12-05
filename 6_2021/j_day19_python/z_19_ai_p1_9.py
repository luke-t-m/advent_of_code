"""Here is a solution to the given problem in Python:

"""
# Parse the input data
data = []
with open('19_input') as f:
    for line in f:
        if line.startswith('---'):
            data.append([])
        else:
            data[-1].append(tuple(map(int, line.strip().split(','))))

# Find pairs of scanners that see at least 12 common beacons
for scanners in itertools.combinations(data, 2):
    # Find the common beacons seen by both scanners
    common = set(scanners[0]).intersection(set(scanners[1]))
    if len(common) >= 12:
        # Calculate the position of the first scanner relative to the second
        pos = [sum(x) for x in zip(*common)]
        pos = [x // len(common) for x in pos]

        # Calculate the orientation of the first scanner relative to the second
        orientation = []
        for i in range(3):
            pos1 = [x[i] for x in scanners[0]]
            pos2 = [x[i] for x in scanners[1]]
            orientation.append(pos1.index(pos[i]) - pos2.index(pos[i]))

        # Print the result
        print(pos, orientation)
"""

This code reads the input data from a file called `19_input` and parses it into a list of beacon positions for each scanner. It then uses the `itertools` module to iterate over all pairs of scanners and find those that see at least 12 common beacons. For each such pair, it calculates the position and orientation of the first scanner relative to the second and prints the result."""