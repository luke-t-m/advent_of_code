"""The problem can be solved by finding pairs of scanners that both see at least 12 of the same beacons. This can be done by reading the input file, parsing the data and storing it in a suitable data structure, and then comparing the data of each pair of scanners to find common beacons.

Here is one possible solution in Python:

"""
# Read the input from the file
with open("19_input", "r") as file:
    data = file.readlines()

# Parse the data and store it in a list of dictionaries, where each dictionary
# represents the data for one scanner
scanners = []
for line in data:
    scanner = {}
    # Split the line into the scanner's ID and the list of beacons
    parts = line.strip().split(":")
    scanner["id"] = int(parts[0])
    scanner["beacons"] = []
    # Split the list of beacons into individual beacon coordinates
    beacon_data = parts[1].strip().split(",")
    for i in range(0, len(beacon_data), 3):
        x = int(beacon_data[i])
        y = int(beacon_data[i + 1])
        z = int(beacon_data[i + 2])
        scanner["beacons"].append((x, y, z))
    scanners.append(scanner)

# Compare the data for each pair of scanners to find common beacons
common_beacon_count = 0
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        # Count the number of common beacons in the two scanners
        common_beacons = set(scanners[i]["beacons"]) & set(scanners[j]["beacons"])
        common_beacon_count = max(common_beacon_count, len(common_beacons))

# Print the result
print(common_beacon_count)
""""""