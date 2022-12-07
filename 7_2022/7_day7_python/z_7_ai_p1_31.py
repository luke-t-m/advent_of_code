"""The first thing to do is to parse the input and construct the file system tree.

We can use a dictionary to store the directory tree. The keys are the directory names and the values are the dictionaries containing the subdirectories and files inside the directory. We also need to keep track of the current directory, so we can use a list to store the path to the current directory.

We can iterate over the input and process each line. If the line starts with `$ cd`, we can update the current directory by either changing to a subdirectory, moving to the parent directory, or changing to the root directory. If the line starts with `$ ls`, we can parse the file and directory names and sizes and add them to the current directory in the tree.

After the input is processed, we can traverse the tree and calculate the total size of each directory by summing the sizes of its files and subdirectories.

Here is the code:

"""
# Parse input
lines = []
with open("7_input") as f:
    lines = f.read().strip().split("\n")

# Construct file system tree
tree = {"/": {"dirs": {}, "size": 0}}
path = ["/"]
for line in lines:
    # Change directory
    if line.startswith("$ cd"):
        _, dir_name = line.split()
        if dir_name == "..":
            # Move to parent directory
            path = path[:-1]
        elif dir_name == "/":
            # Change to root directory
            path = ["/"]
        else:
            # Change to subdirectory
            path.append(dir_name)
    # List directory
    elif line.startswith("$ ls"):
        # Parse file and directory names and sizes
        items = line[3:].strip().split()
        for item in items:
            name, size = item.rsplit(" ", 1)
            size = int(size)
            # Add file or directory to current directory
            if name.startswith("dir"):
                dir_name = name.split()[1]
                if dir_name not in tree[path[-1]]["dirs"]:
                    tree[path[-1]]["dirs"][dir_name] = {"dirs": {}, "size": 0}
            else:
                tree[path[-1]]["size"] += size

# Calculate total size of each directory
def calculate_size(name, tree):
    size = tree[name]["size"]
    for dir_name in tree[name]["dirs"]:
        size += calculate_size(dir_name, tree[name]["dirs"])
    return size

# Find all directories with total size <= 100000
dirs = []
for dir_name, dir_info in tree["/"]["dirs"].items():
    size = calculate_size(dir_name, tree["/"])
    if size <= 100000:
        dirs.append((dir_name, size))

# Calculate the sum of the total sizes of the directories
result = sum(size for _, size in dirs)

# Print the result
print(result)
"""

To run the code, save it to a file (e.g. `main.py"""