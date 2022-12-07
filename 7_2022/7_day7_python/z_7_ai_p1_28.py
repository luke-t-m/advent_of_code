"""Here is a solution in python:

"""
# Parse the input
file_system = {}
current_dir = "/"

with open('7_input') as f:
    for line in f:
        if line.startswith('$ cd'):
            if line.split()[2] == "..":
                # Move to the parent directory
                current_dir = "/".join(current_dir.split("/")[:-1])
            elif line.split()[2] == "/":
                # Move to the root directory
                current_dir = "/"
            else:
                # Move to the specified directory
                current_dir = current_dir + "/" + line.split()[2]
        elif line.startswith('$ ls'):
            # List the files in the current directory
            files = line.split()[2:]
            file_system[current_dir] = files
            
# Compute the total size of each directory            
dir_sizes = {}
for dir, files in file_system.items():
    dir_sizes[dir] = sum(int(f.split(".")[0]) for f in files if "." in f)
    
# Compute the total size of each directory and all of its subdirectories
total_dir_sizes = {}
for dir in dir_sizes.keys():
    total_size = dir_sizes[dir]
    for subdir in dir_sizes.keys():
        if subdir.startswith(dir):
            total_size += total_dir_sizes[subdir]
    total_dir_sizes[dir] = total_size

# Find all directories with a total size of at most 100000
result = 0
for dir, size in total_dir_sizes.items():
    if size <= 100000:
        result += size

# Print the result
print(result)
""""""