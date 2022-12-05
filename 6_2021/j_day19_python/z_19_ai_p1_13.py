"""Here is the solution in Python:

"""
# Read input
with open('19_input') as f:
    data = [line.strip() for line in f.readlines()]

# Parse input
scanners = []
for i in range(0, len(data), 4):
    scanner_id = int(data[i].split()[1][:-1])
    coords = [[int(x) for x in line.split(',')] for line in data[i+2:i+4]]
    scanners.append((scanner_id, coords))

# Find overlaps
overlaps = []
for i in range(len(scanners)):
    for j in range(i+1, len(scanners)):
        overlap = set(scanners[i][1]) & set(scanners[j][1])
        if len(overlap) >= 12:
            overlaps.append((scanners[i][0], scanners[j][0], overlap))

# Print answer
print(overlaps)
"""

First, we read the input from the `19_input` file and parse it into a list of scanners, where each scanner is represented as a tuple containing the scanner's id and a list of the coordinates of the beacons it detects.

Next, we iterate over all pairs of scanners and find the overlapping beacons using the `set` type's `&` operator. If the number of overlapping beacons is at least 12, we add the pair of scanners and the overlapping beacons to the list of overlaps.

Finally, we print the list of overlaps, which is the answer to the problem."""