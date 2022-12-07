"""To solve this problem, we first need to parse the input and build a tree of directories and files. Then, we can traverse the tree and calculate the total size of each directory. Here is how we can do this in Python:

"""
# Parse the input and build the directory tree
directories = {"/": {"size": 0, "directories": {}}}
current_dir = "/"

with open("7_input") as f:
    for line in f:
        line = line.strip()
        if line.startswith("$"):
            # This is a command line
            command, *args = line[1:].split()
            if command == "cd":
                if args[0] == "/":
                    # Change to the root directory
                    current_dir = "/"
                elif args[0] == "..":
                    # Move up one level
                    current_dir = "/".join(current_dir.split("/")[:-1])
                else:
                    # Move down one level
                    current_dir = f"{current_dir}/{args[0]}"
        else:
            # This is a file or directory listing
            size, name = line.split()
            size = int(size)
            if name.startswith("dir"):
                # This is a directory
                name = name[4:]
                if name not in directories[current_dir]["directories"]:
                    directories[current_dir]["directories"][name] = {"size": 0, "directories": {}}
            else:
                # This is a file
                directories[current_dir]["size"] += size

# Traverse the directory tree and calculate the total size of each directory
def calculate_size(dir_path, directories):
    size = directories[dir_path]["size"]
    for name, subdir in directories[dir_path]["directories"].items():
        size += calculate_size(f"{dir_path}/{name}", directories)
    return size

for name, dir_info in directories.items():
    dir_info["size"] = calculate_size(name, directories)

# Find all directories with a total size of at most 100000 and calculate their total size
total_size = 0

for name, dir_info in directories.items():
    if dir_info["size"] <= 100000:
        total_size += dir_info["size"]

# Print the result
print(total_size)
"""

Note that we assumed that the input file is called `7_input`. This code should work as long as the input is in the format described in the problem statement."""