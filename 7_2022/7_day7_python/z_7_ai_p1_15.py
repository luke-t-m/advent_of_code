"""The following is a correct solution to the problem.

"""
directories = ['/']
current_dir = 0

sizes = {}
sizes['/'] = 0

with open('7_input') as f:
  for line in f:
    line = line.strip()
    if line.startswith('$'):
      cmd = line.split()
      if cmd[0] == '$':
        if cmd[1] == 'cd':
          if cmd[2] == '/':
            current_dir = 0
          elif cmd[2] == '..':
            current_dir = directories.index(directories[current_dir].rstrip('/').rsplit('/',1)[0])
          else:
            try:
              current_dir = directories.index(directories[current_dir] + cmd[2] + '/')
            except:
              pass
        elif cmd[1] == 'ls':
          for i in range(2, len(cmd)):
            file = cmd[i].split()
            if file[0] == 'dir':
              if directories[current_dir] == '/':
                directories.append('/' + file[1] + '/')
                sizes['/' + file[1] + '/'] = 0
              else:
                directories.append(directories[current_dir] + file[1] + '/')
                sizes[directories[current_dir] + file[1] + '/'] = 0
            else:
              sizes[directories[current_dir]] += int(file[0])

print(sum([sizes[x] for x in sizes if sizes[x] <= 100000]))
""""""