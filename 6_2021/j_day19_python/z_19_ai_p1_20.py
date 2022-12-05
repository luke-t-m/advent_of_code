"""First, the input must be read from a file called `19_input`. To do this, the following code can be used:

"""
with open('19_input', 'r') as f:
    input_data = f.read()
"""

Next, we need to parse the input data and extract the positions of the beacons detected by each scanner. We can use regular expressions to do this. The following code uses the `re` module to extract the positions of the beacons detected by each scanner:

"""
import re

# Use a regular expression to extract the positions of the beacons detected by each scanner
beacon_positions = re.findall(r'(-?\d+,-?\d+,-?\d+)', input_data)
"""

Next, we need to find pairs of scanners that have overlapping detection regions such that there are at least 12 beacons that both scanners detect within the overlap. To do this, we can iterate over all pairs of scanners and check if they have at least 12 beacons in common. If they do, we can add the scanners to a list of scanner pairs. The following code uses a `Counter` from the `collections` module to count the number of beacons that each scanner detects, and then uses a nested loop to find pairs of scanners that have at least 12 beacons in common:

"""
from collections import Counter

# Count the number of beacons that each scanner detects
beacon_counts = Counter(beacon_positions)

# Initialize a list to store the pairs of scanners
scanner_pairs = []

# Iterate over all pairs of scanners
for scanner_1, count_1 in beacon_counts.items():
    for scanner_2, count_2 in beacon_counts.items():
        # Check if the scanners have at least 12 beacons in common
        if scanner_1 != scanner_2 and count_1 >= 12 and count_2 >= 12:
            scanner_pairs.append((scanner_1, scanner_2))
"""

Finally, we can print the list of scanner pairs by using the following code:

"""
print(scanner_pairs)