"""To solve this problem, we need to parse the input, build a filesystem tree, and traverse it to find all the directories with total size of at most 100000.

First, let's parse the input. We can use regular expressions to extract the commands and the output from each line of the input. The following code does this:

"""
import re

# Parse the input
commands = []
outputs = []
with open('7_input') as f:
  for line in f:
    # Extract the commands
    m = re.match(r'\$ (cd|ls) (.*)', line)
    if m:
      commands.append(m.groups())
    else:
      outputs.append(line.strip())
"""

Next, we need to build the filesystem tree. We can do this by simulating the execution of the commands. For each `cd` command, we move to the corresponding directory. For each `ls` command, we add the files and directories in the current directory to the tree. The following code does this:

"""
# Build the filesystem tree
current_dir = '/'
filesystem = {
  '/': {
    'type': 'dir',
    'size': 0,
    'contents': {},
  },
}

for cmd, arg in commands:
  if cmd == 'cd':
    if arg == '/':
      current_dir = '/'
    elif arg == '..':
      current_dir = '/'.join(current_dir.split('/')[:-1])
    else:
      current_dir += '/' + arg
  elif cmd == 'ls':
    # Add the files and directories to the current directory
    for item in outputs.pop(0).split():
      # Check if the item is a file or a directory
      if item.startswith('dir'):
        item_type = 'dir'
        item_name = item.split()[1]
      else:
        item_type = 'file'
        item_name, item_size = item.split()
        item_size = int(item_size)

      # Add the item to the filesystem tree
      filesystem[current_dir]['contents'][item_name] = {
        'type': item_type,
        'size': item_size,
        'contents': {},
      }
"""

Now that we have the filesystem tree, we can traverse it to find the directories with total size of at most 100000. We need to keep track of the total size of each directory as we traverse the tree. The following code does this:

"""
# Find the directories with total size of at most 100000
dirs = []

def traverse(dir_name, total_size):
  # Update the total size of the current directory
  filesystem[dir_name]['size'] = total_size

  # Check if the current directory is a candidate for deletion
  if total_size <= 100000:
    dirs.append(dir_name)

  # Traverse the contents of the current directory
  for item_name, item in filesystem[dir_name]['contents'].items():
    if item['type'] == 'dir':
      traverse(dir_name + '/' + item_name, total_size + item['size'])

