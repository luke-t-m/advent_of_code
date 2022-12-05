"""To solve this problem, you need to read the input from a file called `19_input`. Then, you need to find pairs of scanners that have overlapping detection regions such that there are at least 12 beacons that both scanners detect within the overlap.

Here is a sample solution in Python:

"""
# Read the input from the file
with open("19_input", "r") as f:
  scanner_data = f.readlines()

# Parse the input data into a dictionary where the keys are the scanner ids and the values
# are the detected beacons relative to the scanner
scanners = {}
for i in range(0, len(scanner_data), 2):
  scanner_id = int(scanner_data[i].strip()[8:])
  detected_beacons = []
  for line in scanner_data[i+1].strip().split("\n"):
    detected_beacons.append(tuple(map(int, line.strip().split(","))))
  scanners[scanner_id] = detected_beacons

# Find pairs of scanners that have overlapping detection regions with at least 12 beacons in common
for scanner1_id, scanner1_beacons in scanners.items():
  for scanner2_id, scanner2_beacons in scanners.items():
    if scanner1_id == scanner2_id:
      continue
    common_beacons = set(scanner1_beacons).intersection(set(scanner2_beacons))
    if len(common_beacons) >= 12:
      print(f"Found overlapping scanners: {scanner1_id} and {scanner2_id}")
"""

This code reads the input from the file, parses the data into a dictionary where the keys are the scanner ids and the values are the detected beacons relative to the scanner. It then finds pairs of scanners that have overlapping detection regions with at least 12 beacons in common and prints the scanner id for each pair.

To run this code, save it to a file called `solution.py` and run it using the following command:

"""
python solution.py
""""""