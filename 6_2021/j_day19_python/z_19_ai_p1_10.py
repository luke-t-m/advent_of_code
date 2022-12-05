"""The first step is to parse the input and store the data in a convenient data structure. The input consists of a number of scanner reports, each of which contains a number of beacon positions. We will store each scanner report as a list of beacon positions, where each beacon position is a tuple of three numbers.

We will use a dictionary to store the data, where the keys are the scanner numbers and the values are the lists of beacon positions for each scanner.

The following code reads the input from the file `19_input` and stores it in the dictionary `scanners`:

"""
scanners = {}

with open("19_input") as f:
    scanner_num = None
    for line in f:
        line = line.strip()
        if line.startswith("--- scanner"):
            scanner_num = int(line.split()[2])
            scanners[scanner_num] = []
        elif line:
            x, y, z = map(int, line.split(","))
            scanners[scanner_num].append((x, y, z))
"""

The next step is to find pairs of scanners that have overlapping detection regions and at least 12 common beacons. To do this, we will loop over all pairs of scanners and check whether their detection regions overlap and whether they have at least 12 common beacons. If a pair of scanners satisfies these conditions, we will add the scanner numbers and the common beacons to a list.

The following code finds all pairs of scanners that have overlapping detection regions and at least 12 common beacons:

"""
pairs = []
for i, (scanner1, beacons1) in enumerate(scanners.items()):
    for scanner2, beacons2 in scanners.items()[i + 1:]:
        # Calculate the overlap of the detection regions
        # ...
        
        # Calculate the common beacons
        # ...
        
        if overlap and len(common_beacons) >= 12:
            pairs.append((scanner1, scanner2, common_beacons))
"""

To calculate the overlap of the detection regions, we will loop over all beacons in the first scanner and check whether they are within 1000 units of any beacon in the second scanner. If a beacon in the first scanner is within 1000 units of any beacon in the second scanner, we will add it to the list of overlapping beacons.

The following code calculates the overlap of the detection regions for two scanners:

"""
overlap = []
for x1, y1, z1 in beacons1:
    for x2, y2, z2 in beacons2:
        if abs(x1 - x2) <= 1000 and abs(y1 - y2) <= 1000 and abs(z1 - z2) <= 1000:
            overlap.append((x1, y1, z1))
"""

To calculate the common beacons, we will loop over all overlapping beacons and check whether they are present in both scanners. If a beacon is present in both scanners, we will add it to the list of common beacons.

The following code calculates the common beacons for two scanners:

"""
common_beacons = []
for x, y, z in overlap:
    if (x, y, z) in beacons1 and (x, y, z) in beacons2:
        common_beacons.append((x"""