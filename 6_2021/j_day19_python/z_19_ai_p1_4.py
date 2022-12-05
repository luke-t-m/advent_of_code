"""To solve this problem, we need to find pairs of scanners that both see at least 12 of the same beacons. We can do this by reading in the scanner data from the input file and then comparing each pair of scanners to see if they have at least 12 beacons in common. If they do, we can add them to a list of scanner pairs that we can use to reconstruct the beacon map. Here is a possible solution in Python:

"""
# Read in the scanner data from the input file
with open("19_input") as f:
    scanner_data = f.readlines()

# Parse the scanner data into a list of scanners
scanners = []
for scanner in scanner_data:
    scanner_beacons = scanner.strip().split("\n")
    scanner_beacons = [tuple(map(int, beacon.split(","))) for beacon in scanner_beacons]
    scanners.append(scanner_beacons)

# Compare each pair of scanners to see if they have at least 12 beacons in common
scanner_pairs = []
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        common_beacons = set(scanners[i]) & set(scanners[j])
        if len(common_beacons) >= 12:
            scanner_pairs.append((i, j))

# Print the list of scanner pairs that we can use to reconstruct the beacon map
print(scanner_pairs)
""""""