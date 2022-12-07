"""The following code solves the problem as described in the prompt.

"""
# Parse input and build filesystem tree
filesystem = {}
path = ["/"]
for line in open("7_input"):
  # Handle cd commands
  if line[0] == "$":
    parts = line.strip().split()
    if parts[1] == "cd":
      if parts[2] == "/":
        path = ["/"]
      elif parts[2] == "..":
        path.pop()
      else:
        path.append(parts[2])
  # Handle ls commands
  else:
    parts = line.strip().split()
    if parts[0] == "dir":
      cur = filesystem
      for directory in path:
        if directory not in cur:
          cur[directory] = {}
        cur = cur[directory]
      cur[parts[1]] = {}
    else:
      cur = filesystem
      for directory in path:
        cur = cur[directory]
      cur[parts[1]] = int(parts[0])

# Recursive function to calculate size of directory and its subdirectories
def dir_size(directory):
  total_size = 0
  for name, item in directory.items():
    if type(item) == int:
      total_size += item
    else:
      total_size += dir_size(item)
  return total_size

# Find all directories with size <= 100000 and calculate their total size
total_size = 0
for name, directory in filesystem["/"].items():
  size = dir_size(directory)
  if size <= 100000:
    total_size += size

# Print the answer
print(total_size)
""""""