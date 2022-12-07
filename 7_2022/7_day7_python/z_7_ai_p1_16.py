"""Here is a solution to the problem in Python:

"""
# Parse the input file to get the data
with open("7_input", "r") as f:
  data = f.readlines()

# Create a dictionary to store the sizes of each directory
sizes = {}

# Initialize the current directory to /
cur_dir = "/"

# Loop through the input data
for line in data:
  # If this line is a command, process it
  if line[0] == "$":
    # If the command is "cd", update the current directory
    if line[:3] == "cd ":
      if line[3:] == "..\n":
        # If the argument is "..", move up one level
        cur_dir = cur_dir[:cur_dir.rfind("/")]
      elif line[3:] == "/\n":
        # If the argument is "/", move to the outermost directory
        cur_dir = "/"
      else:
        # Otherwise, move into the specified directory
        cur_dir += line[3:-1]
    elif line[:3] == "ls":
      # If the command is "ls", process the output
      items = line[3:].split()
      # Loop through the items in the output
      for item in items:
        # If the item is a file, add its size to the current directory
        if item.find(".") != -1:
          sizes[cur_dir] += int(item[:item.find(".")])
        # If the item is a directory, add its size to the current directory
        # if it has been calculated, or initialize its size to 0
        else:
          if item not in sizes:
            sizes[item] = 0
          sizes[cur_dir] += sizes[item]

# Initialize the total size to 0
total_size = 0

# Loop through the directories and add the ones with size <= 100000 to the total size
for dir, size in sizes.items():
  if size <= 100000:
    total_size += size

# Print the total size
print(total_size)
"""

To run this code, you will need to save it to a file called `solution.py`, and then run it using the command `python solution.py`. The answer will be printed to the terminal."""