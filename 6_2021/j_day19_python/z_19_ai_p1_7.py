"""The problem can be solved by following these steps:

1. Parse the input file and extract the list of beacons detected by each scanner.
2. Find pairs of scanners that have at least 12 beacons in common.
3. Use the pairs of scanners to build a map of the region.
4. Determine the positions of the scanners and beacons in the map.
5. Print the answer.

Here is a possible solution in Python:

"""
# Parse the input and extract the list of beacons detected by each scanner
beacons = {}
with open("19_input") as f:
    for line in f:
        scanner, *b = line.strip().split()
        beacons[scanner] = [tuple(map(int, b[i:i+3])) for i in range(0, len(b), 3)]

# Find pairs of scanners that have at least 12 beacons in common
pairs = []
for s1, b1 in beacons.items():
    for s2, b2 in beacons.items():
        if s1 == s2: continue
        common = set(b1) & set(b2)
        if len(common) >= 12:
            pairs.append((s1, s2))

# Use the pairs of scanners to build the map of the region
map = {}
for s1, s2 in pairs:
    b1, b2 = beacons[s1], beacons[s2]
    common = set(b1) & set(b2)
    # Determine the relative positions of the scanners
    x1, y1, z1 = b1[0]
    x2, y2, z2 = b2[0]
    dx, dy, dz = x2-x1, y2-y1, z2-z1
    map[s1] = (x1, y1, z1, dx, dy, dz)
    map[s2] = (x2, y2, z2, dx, dy, dz)
    # Add the common beacons to the map
    for x, y, z in common:
        map[x, y, z] = (x+dx, y+dy, z+dz)

# Determine the positions of the scanners and beacons in the map
positions = {}
for (x, y, z), (x2, y2, z2, dx, dy, dz) in map.items():
    if (dx, dy, dz) == (0, 0, 0):
        positions[x, y, z] = (x2, y2, z2)
    else:
        positions[x2, y2, z2] = (x, y, z)

# Print the answer
x_values = [x for x, _, _ in positions.values()]
y_values = [y for _, y, _ in positions.values()]
z_values = [z for _, _, z in positions.values()]
x_min, x_max = min(x_values), max(x_values)
y_min, y_max = min(y_values), max(y_values)
z_min, z_max = min(z_values), max(z_values)
print(x_"""