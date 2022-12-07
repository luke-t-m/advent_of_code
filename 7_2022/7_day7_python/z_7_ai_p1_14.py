"""This problem can be solved by traversing the tree of directories and files in a depth-first manner and keeping track of the sizes of the directories.

First, we need to parse the input and create a tree structure that represents the filesystem. We can do this by keeping track of the current directory and the directories and files that are directly contained by it. When we encounter a `cd` command, we update the current directory, and when we encounter a `ls` command, we add the directories and files that are listed to the current directory.

Once we have the tree, we can traverse it in a depth-first manner, summing up the sizes of the files in each directory and storing them in a dictionary, keyed by the directory name.

To find the directories with a total size of at most 100000, we can iterate over the dictionary of sizes and keep track of the directories that satisfy this condition. Finally, we can sum up the sizes of these directories to get the answer.

Here is the code:

"""
# Parse the input and create the tree structure
current_dir = '/'
directories = {current_dir: {'dirs': [], 'files': []}}
with open('7_input') as f:
  for line in f:
    if line[0] == '$':
      # Parse the command
      cmd, *args = line[1:].strip().split()
      if cmd == 'cd':
        # Update the current directory
        if args[0] == '/':
          current_dir = '/'
        elif args[0] == '..':
          current_dir = current_dir.rstrip('/').rsplit('/', 1)[0]
        else:
          current_dir += args[0] + '/'
          if current_dir not in directories:
            directories[current_dir] = {'dirs': [], 'files': []}
      elif cmd == 'ls':
        # Add the directories and files to the current directory
        for item in args:
          if item.endswith('/'):
            directories[current_dir]['dirs'].append(item.rstrip('/'))
          else:
            name, size = item.split()
            directories[current_dir]['files'].append((name, int(size)))

# Traverse the tree and keep track of the sizes of the directories
dir_sizes = {}
stack = [('/', 0)]
while stack:
  dirname, size = stack.pop()
  # Add the sizes of the files in the current directory
  for name, size in directories[dirname]['files']:
    size += size
  # Add the current directory to the dictionary of sizes
  dir_sizes[dirname] = size
  # Add the subdirectories to the stack
  for subdir in directories[dirname]['dirs']:
    stack.append((dirname + subdir + '/', size))

# Find the directories with a total size of at most 100000
small_dirs = [dirname for dirname, size in dir_sizes.items() if size <= 100000]

# Calculate the sum of the sizes of these directories
answer = sum(dir_sizes[dirname] for dirname in small_dirs)

# Print the answer
print(answer)
""""""