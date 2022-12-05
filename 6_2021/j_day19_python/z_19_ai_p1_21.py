"""To solve this problem, you will need to read the input from the file called "19_input", which contains the data for the scanners. Then, you need to find pairs of scanners that have overlapping detection regions, such that there are at least 12 beacons that both scanners detect within the overlap. Once you have found these pairs of scanners, you can use them to reconstruct the beacon map one scanner at a time.

Here is a sample solution in Python:

"""
# Read the input from the file
with open("19_input") as f:
    data = f.read()

# Parse the input to extract the positions of the scanners and beacons
scanner_data = {}
for line in data.split("\n"):
    if not line.startswith("--- scanner"):
        continue
    scanner_id = int(line.split(" ")[-1])
    scanner_data[scanner_id] = []
    for coord in data.split("\n")[1:]:
        x, y, z = map(int, coord.split(","))
        scanner_data[scanner_id].append((x, y, z))

# Find pairs of scanners that have at least 12 overlapping beacons
overlapping_pairs = []
for scanner_id1, scanner1 in scanner_data.items():
    for scanner_id2, scanner2 in scanner_data.items():
        if scanner_id1 == scanner_id2:
            continue
        common_beacons = set(scanner1) & set(scanner2)
        if len(common_beacons) >= 12:
            overlapping_pairs.append((scanner_id1, scanner_id2))

# Print the pairs of scanners with overlapping detection regions
print(overlapping_pairs)
""""""