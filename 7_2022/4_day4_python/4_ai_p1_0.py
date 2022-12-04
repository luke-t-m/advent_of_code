def solve():
  counter = 0
  # Open the input file
  with open('4_input', 'r') as file:
    # Iterate through each line in the file
    for line in file:
      # Split the line into a pair of ranges
      ranges = line.strip().split(',')
      # Get the start and end of each range
      range1 = list(map(int, ranges[0].split('-')))
      range2 = list(map(int, ranges[1].split('-')))
      # Check if one range fully contains the other
      if (range1[0] <= range2[0] and range1[1] >= range2[1]) or (range2[0] <= range1[0] and range2[1] >= range1[1]):
        # Increase the counter if this is the case
        counter += 1
  # Return the counter
  return counter

# Call the function and print the result
print(solve())
