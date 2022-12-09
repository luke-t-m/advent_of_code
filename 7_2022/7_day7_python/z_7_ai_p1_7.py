"""The prompt suggests that we need to calculate the total size of all directories with a total size of at most 100000. To solve this problem, we need to first parse the input data and build the filesystem tree. We can then traverse the tree and calculate the total size of each directory.

Here is one possible solution in Python:

"""
# Parse the input data and build the filesystem tree
with open('7_test') as f:
  lines = f.readlines()

fs = {'.': {'name': '.', 'parent': None, 'children': [], 'size': 0}}
curr_dir = '.'

for line in lines:
  line = line.strip()
  if line.startswith('$'):
    cmd = line[2:].split()
    if cmd[0] == 'cd':
      if cmd[1] == '/':
        curr_dir = '.'
      elif cmd[1] == '..':
        curr_dir = fs[curr_dir]['parent']
      else:
        curr_dir = curr_dir + '/' + cmd[1]
  else:
    parts = line.split()
    if parts[0] == 'dir':
      fs[curr_dir + '/' + parts[1]] = {'name': parts[1], 'parent': curr_dir, 'children': [], 'size': 0}
    else:
      fs[curr_dir]['children'].append(parts[1])
      fs[curr_dir]['size'] += int(parts[0])

# Traverse the tree and calculate the total size of each directory
for dir in fs:
  for child in fs[dir]['children']:
    if child in fs:
      fs[dir]['size'] += fs[dir + '/' + child]['size']

# Find all directories with total size at most 100000 and calculate their sum
result = 0
for dir in fs:
  if fs[dir]['size'] <= 100000:
    result += fs[dir]['size']

print(result)
""""""