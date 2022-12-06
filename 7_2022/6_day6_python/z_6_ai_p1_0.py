# Read the datastream from the input file
with open('6_input', 'r') as f:
  datastream = f.read()

# Initialize the list of last four characters seen to be empty
last_four = []

# Iterate over the characters in the datastream
for i, c in enumerate(datastream):
  # Add the current character to the list of last four characters
  last_four.append(c)

  # If we have seen at least four characters, check if they are all different
  if len(last_four) >= 4:
    # If they are, print the number of characters processed and stop iterating
    if len(set(last_four)) == 4 and i > 7:
      print(i + 1)
      break

  # If we have seen more than four characters, remove the oldest character from the list
  if len(last_four) > 4:
    last_four.pop(0)