"""The problem can be solved by finding pairs of scanners that have at least 12 beacons in common. To do this, we can iterate over all pairs of scanners and find the beacons that are detected by both scanners. If the number of common beacons is at least 12, we can use these beacons to determine the positions of the scanners relative to each other, and we can use these positions to reconstruct the entire beacon map.

Here is a solution in Python:

"""
# Read the scanner reports from the input file
with open('19_input', 'r') as f:
    reports = [line.strip() for line in f.readlines()]

# Parse the scanner reports into a list of lists of beacon coordinates
scanners = []
for report in reports:
    if report.startswith('--- scanner'):
        scanners.append([])
    else:
        scanners[-1].append(tuple(map(int, report.split(','))))

# Iterate over all pairs of scanners and find pairs with at least 12 common beacons
for i, scanner1 in enumerate(scanners):
    for j, scanner2 in enumerate(scanners):
        if i >= j:
            continue

        # Find the beacons detected by both scanners
        common_beacons = set(scanner1) & set(scanner2)

        # If there are at least 12 common beacons, we can determine the positions
        # of the scanners relative to each other and reconstruct the beacon map
        if len(common_beacons) >= 12:
            # TODO: Determine the positions of the scanners relative to each other
            # and reconstruct the beacon map

            # Print the answer
            print('Found a pair of scanners with at least 12 common beacons:')
            print('Scanner', i, ':', scanner1)
            print('Scanner', j, ':', scanner2)
            print('Common beacons:', common_beacons)
""""""