"""To solve this problem, we need to implement a file system parser that will read the commands and output from the input file and keep track of the directory structure and file sizes. We can then traverse the directory tree to calculate the total sizes of each directory and find the directories with total sizes of at most 100000. The sum of these directories' total sizes can then be calculated and printed as the answer.

Here is one possible implementation in Python:

"""
# Read the input from the file
with open("7_input") as input_file:
    lines = input_file.readlines()

# Parse the input and build the directory tree
directories = {"/": {"size": 0, "children": {}}}
current_dir = directories["/"]
for line in lines:
    # If this line is a command, parse it and execute it
    if line[0] == "$":
        command, *args = line.strip().split(" ")
        if command == "cd":
            # If the command is "cd", change the current directory
            if args[0] == "/":
                # If the argument is "/", change the current directory to the root directory
                current_dir = directories["/"]
            elif args[0] == "..":
                # If the argument is "..", change the current directory to its parent directory
                parent_dir = current_dir["parent"]
                if parent_dir is not None:
                    current_dir = parent_dir
            else:
                # Otherwise, change the current directory to the specified child directory
                child_dir = args[0]
                if child_dir in current_dir["children"]:
                    current_dir = current_dir["children"][child_dir]
        elif command == "ls":
            # If the command is "ls", list the files and directories in the current directory
            for item in args:
                # Check if this item is a file or a directory
                if "." in item:
                    # If it contains a ".", it is a file
                    # Parse the size of the file and add it to the current directory's size
                    size = int(item.split(" ")[0])
                    current_dir["size"] += size
                else:
                    # Otherwise, it is a directory
                    # Create a new entry for the directory in the current directory's children
                    dir_name = item.split(" ")[1]
                    current_dir["children"][dir_name] = {
                        "size": 0,
                        "children": {},
                        "parent": current_dir,
                    }

# Traverse the directory tree to find all directories with total sizes at most 100000
small_dirs = []
stack = [directories["/"]]
while len(stack) > 0:
    # Pop the top directory from the stack
    dir = stack.pop()
    # Calculate the total size of the directory by summing the sizes of its children
    total_size = dir["size"]
    for child in dir["children"].values():
        total_size += child["size"]
        # If the child is a directory, add it to the stack to be visited later
        if len(child["children"]) > 0:
            stack.append(child)
    # If the total size is at most 100000, add it to the list of small directories
    if total_size"""