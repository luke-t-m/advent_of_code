"""The problem is to find pairs of scanners such that they detect at least 12 common beacons. The solution is to read the scanner data from the file, iterate over the scanner pairs and calculate the common beacons detected by each pair. Then, find the pairs that have at least 12 common beacons and print them.

Here is a possible implementation in Python:

"""
# Read the scanner data from the file
with open('19_input', 'r') as f:
  data = f.readlines()

# Parse the scanner data into a dictionary, where the keys are the scanner ids and the values are the lists of beacons detected by each scanner
scanners = {}
for line in data:
  line = line.strip()
  if line.startswith('--- scanner'):
    # This line contains the scanner id
    scanner_id = int(line.split()[2])
    scanners[scanner_id] = []
  else:
    # This line contains the coordinates of a beacon detected by the current scanner
    x, y, z = map(int, line.split(','))
    scanners[scanner_id].append((x, y, z))

# Iterate over the scanner pairs and calculate the common beacons detected by each pair
for scanner_id_1, beacons_1 in scanners.items():
  for scanner_id_2, beacons_2 in scanners.items():
    if scanner_id_1 >= scanner_id_2:
      # Skip this pair because it has been already processed or it is the same scanner
      continue
    # Calculate the common beacons detected by the two scanners
    common_beacons = set(beacons_1) & set(beacons_2)
    if len(common_beacons) >= 12:
      # Print the scanner pair and the common beacons detected by the two scanners
      print(f'scanner {scanner_id_1} and scanner {scanner_id_2} have {len(common_beacons)} common beacons: {common_beacons}')
""""""