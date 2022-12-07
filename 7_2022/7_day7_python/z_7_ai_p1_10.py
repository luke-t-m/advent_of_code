"""The following code calculates the total size of each directory in the given file system and prints the sum of the sizes of all directories with a total size of at most 100000.

"""python
import re

# Parse the input
with open("7_input") as f:
    lines = f.readlines()

# Create a dictionary to store the total size of each directory
dirs = {}

# Initialize the current directory to the outermost directory
cur_dir = "/"

# Parse each line in the input
for line in lines:
    # Check if the line is a command
    if line[0] == "$":
        # Parse the command and its arguments
        command, args = re.match("^\$ (\w+) (.*)$", line).groups()

        # Check the type of command and update the current directory accordingly
        if command == "cd":
            if args == "/":
                cur_dir = "/"
            elif args == "..":
                cur_dir = "/".join(cur_dir.split("/")[:-1])
            else:
                cur_dir = f"{cur_dir}/{args}"

    # Otherwise, the line is a directory listing
    else:
        # Split the line into its individual items
        items = line.split()

        # Iterate over the items
        for item in items:
            # Check if the item is a directory
            if item.startswith("dir"):
                # Extract the directory name
                name = item.split("dir ")[1]

                # Initialize the total size of the directory to 0
                dirs[name] = 0
            # Otherwise, the item is a file
            else:
                # Extract the file size
                size = int(item)

                # Add the size of the file to the total size of the current directory
                dirs[cur_dir] += size

# Calculate the sum of the sizes of all directories with a total size of at most 100000
result = sum(size for size in dirs.values() if size <= 100000)

# Print the result
print(result)
""""""