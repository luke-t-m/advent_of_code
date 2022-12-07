"""To solve this problem, we need to first parse the input to create a data structure that represents the directory tree. Then we can traverse the tree to calculate the total size of each directory and find all directories with a total size of at most 100000. Finally, we can sum the total sizes of these directories to find the answer.

Here is one way to solve this problem in Python:

"""
# Parse the input to create the directory tree
directories = {}
current_directory = "/"
for line in open("7_input"):
    line = line.strip()
    if line.startswith("$"):
        # This is a command line
        command, *args = line[1:].split()
        if command == "cd":
            # Change directory
            if args[0] == "/":
                # Move to the root directory
                current_directory = "/"
            elif args[0] == "..":
                # Move to the parent directory
                current_directory = current_directory.rpartition("/")[0]
            else:
                # Move to a child directory
                current_directory = current_directory + "/" + args[0]
        elif command == "ls":
            # List the contents of the current directory
            for item in args:
                if item.startswith("dir"):
                    # This is a directory
                    directory = item[3:].strip()
                    if directory not in directories:
                        directories[directory] = {}
                else:
                    # This is a file
                    file, size = item.split()
                    directories[current_directory][file] = int(size)

# Traverse the directory tree to calculate the total size of each directory
def calculate_directory_size(directory, directories):
    # Calculate the total size of the files in the current directory
    size = sum(directories[directory].values())

    # Add the total size of each subdirectory
    for subdirectory in directories[directory]:
        size += calculate_directory_size(subdirectory, directories)

    return size

total_sizes = {}
for directory in directories:
    total_sizes[directory] = calculate_directory_size(directory, directories)

# Find all directories with a total size of at most 100000 and sum their total sizes
ans = sum(size for size in total_sizes.values() if size <= 100000)

# Print the answer
print(ans)
""""""