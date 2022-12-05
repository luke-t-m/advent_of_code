"""This problem can be solved by finding pairs of scanners that see at least 12 of the same beacons. We can use this information to determine the relative positions of the scanners, which will allow us to reconstruct the map of the region.

Here is a solution in Python:

"""
# Parse the input data
data = []
with open('19_input') as f:
  for line in f:
    if line.startswith('---'):
      data.append([])
    else:
      data[-1].append(tuple(map(int, line.strip().split(','))))

# Find pairs of scanners that see at least 12 of the same beacons
pairs = []
for i in range(len(data)):
  for j in range(i+1, len(data)):
    common = set(data[i]) & set(data[j])
    if len(common) >= 12:
      pairs.append((i, j, common))

# Use the pairs to determine the relative positions of the scanners
scanners = []
for i, j, common in pairs:
  # Compute the centroids of the two scanners
  centroid1 = sum(data[i]) / len(data[i])
  centroid2 = sum(data[j]) / len(data[j])
  # Compute the relative positions of the scanners
  pos1 = centroid1 - centroid2
  pos2 = centroid2 - centroid1
  # Add the scanners to the list of scanners
  scanners.append((pos1, data[i]))
  scanners.append((pos2, data[j]))

# Print the answer
answer = 0
for pos, beacons in scanners:
  for beacon in beacons:
    answer += sum(abs(pos + beacon))
print(answer)
""""""