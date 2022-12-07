"""The following code finds all directories with a total size of at most 100,000, then calculates the sum of their total sizes.

"""
directories = {"/": 0}
current_dir = "/"
with open("7_input") as f:
  for line in f:
    if line[0] == "$":
      command = line.split()
      if command[1] == "cd":
        if command[2] == "/":
          current_dir = "/"
        elif command[2] == "..":
          current_dir = "/".join(current_dir.split("/")[:-1])
        else:
          current_dir += "/" + command[2]
      elif command[1] == "ls":
        files = command[2:]
        for file in files:
          size, name = file.split()
          directories[current_dir] += int(size)
          
sum = 0
for directory in directories:
  if directories[directory] <= 100000:
    sum += directories[directory]
    
print(sum)
""""""