"""To solve this problem, we first need to parse the input data. We can do this by reading each line of the input file and storing the scanner data in a dictionary. The keys of the dictionary will be the scanner IDs, and the values will be the lists of detected beacons.

Once we have parsed the input data, we can loop through each pair of scanners and find the overlap between their detected beacons. If the overlap contains at least 12 beacons, we can use this overlap to determine the positions of the scanners relative to each other.

To determine the positions of the scanners, we can first find the centroid of the overlap region. This will give us a point that is the center of the overlap region. Then, we can find the vector between the centroid and each scanner's position. This vector will give us the direction and distance from the scanner to the centroid.

Once we have determined the positions of the scanners, we can use this information to determine the positions of the beacons. To do this, we can loop through each scanner and find the beacons that it detects. We can then use the scanner's position and the relative positions of the beacons to determine the absolute positions of the beacons.

Finally, we can print the positions of the beacons as the solution to the problem. Here is some sample code that demonstrates how to solve this problem:

"""
# Parse the input data
scanners = {}
with open('19_input') as f:
    for line in f:
        # Read the scanner ID and the detected beacons
        parts = line.strip().split(':')
        scanner_id = parts[0].strip()
        detected_beacons = parts[1].strip().split(',')
        # Store the scanner data in a dictionary
        scanners[scanner_id] = detected_beacons

# Loop through each pair of scanners and find the overlap
for scanner1_id, scanner1_beacons in scanners.items():
    for scanner2_id, scanner2_beacons in scanners.items():
        # Skip if the scanners are the same
        if scanner1_id == scanner2_id:
            continue
        # Find the overlap between the two scanners
        overlap = set(scanner1_beacons) & set(scanner2_beacons)
        # Check if the overlap contains at least 12 beacons
        if len(overlap) >= 12:
            # Determine the positions of the scanners
            # Find the centroid of the overlap region
            centroid = calculate_centroid(overlap)
            # Find the vector between the centroid and each scanner's position
            vector1 = calculate_vector(centroid, scanner1_position)
            vector2 = calculate_vector(centroid, scanner2_position)
            # Use the vectors to determine the positions of the scanners
            scanner1_position = determine_position(centroid, vector1)
            scanner2_position = determine_position(centroid, vector2)

# Determine the positions of the beacons
beacons = {}
for scanner_id, scanner_beacons in scanners.items():
    # Find the scanner's position
    scanner_position = scanners[scanner_id]
    # Loop through each detected beacon
    for beacon in scanner_beacons:
        # Determine the beacon's absolute position
        beacon_position = determine_position(scanner_position, beacon)
        # Store the beacon position in a dictionary"""