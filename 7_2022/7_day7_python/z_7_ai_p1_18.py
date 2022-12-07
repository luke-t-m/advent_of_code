"""To solve this problem, we need to parse the input to build the file system tree and then traverse the tree to calculate the total size of each directory.

Here is a possible solution:

"""
# Parse the input and build the file system tree
tree = {}
with open('7_input') as f:
  path = []
  for line in f:
    # Remove the leading $ character
    line = line[1:].strip()
    if line.startswith('cd'):
      # Handle the cd command
      dir_name = line.split()[1]
      if dir_name == '/':
        # Switch to the root directory
        path = []
      elif dir_name == '..':
        # Move one level up in the directory tree
        path.pop()
      else:
        # Move one level down in the directory tree
        path.append(dir_name)
    elif line.startswith('ls'):
      # Handle the ls command
      items = line.split()[1:]
      curr_dir = tree
      # Navigate to the current directory in the tree
      for dir_name in path:
        curr_dir = curr_dir[dir_name]
      # Add the items in the current directory to the tree
      for item in items:
        if item.startswith('dir'):
          # Add a new directory
          curr_dir[item.split('dir')[1].strip()] = {}
        else:
          # Add a new file
          file_name, file_size = item.split()
          curr_dir[file_name] = int(file_size)

# Traverse the tree and calculate the total size of each directory
def calculate_size(tree):
  # Base case: the current node is a file, return its size
  if isinstance(tree, int):
    return tree
  # Recursive case: the current node is a directory,
  # calculate the total size by summing the sizes of its children
  total_size = 0
  for item in tree.values():
    total_size += calculate_size(item)
  return total_size

# Calculate the total size of the root directory
total_size = calculate_size(tree)

# Find all the directories with a total size of at most 100000
# and calculate their total size
total = 0
for dir_name, dir_tree in tree.items():
  dir_size = calculate_size(dir_tree)
  if dir_size <= 100000:
    total += dir_size

# Print the answer
print(total)
""""""