"""The first step is to parse the input into a representation of the file system hierarchy. Since the input specifies the commands that were run to obtain the file system hierarchy, we can simulate these commands to obtain the hierarchy.

We can use a stack to keep track of the current directory as we navigate through the file system. We start at the root directory, represented by the string "/". Whenever we encounter a "cd" command, we either push a new directory onto the stack, or pop a directory from the stack depending on whether the argument to the "cd" command is ".." or not. Whenever we encounter an "ls" command, we add the files and directories listed in the output of the command to the current directory.

Once we have the file system hierarchy, we can traverse the hierarchy and calculate the total size of each directory. To do this, we can use a recursive function that takes a directory as input and returns the total size of that directory. If the input directory is a file, we simply return the size of that file. If the input directory is a directory, we recursively calculate the total size of each of its children, sum the sizes of all of the children, and return the result.

The final step is to find all of the directories with a total size of at most 100000 and sum their total sizes. We can do this by simply traversing the file system hierarchy and keeping track of the directories with a total size of at most 100000 as we calculate the total size of each directory.

Here is a solution in Python:

"""
# Parse the input into a representation of the file system hierarchy
curr_dir = ["/"]
file_system = {"/": {"type": "dir", "children": {}}}

with open("7_input", "r") as f:
    for line in f:
        if line[0] == "$":
            # Parse the command and its arguments
            parts = line[1:].strip().split()
            cmd = parts[0]
            args = parts[1:]

            if cmd == "cd":
                # Change directory
                if args[0] == "..":
                    curr_dir.pop()
                else:
                    curr_dir.append(args[0])

                    # Create the directory if it doesn't already exist
                    path = "/".join(curr_dir)
                    if path not in file_system:
                        file_system[path] = {"type": "dir", "children": {}}
            elif cmd == "ls":
                # List the contents of the current directory
                for item in args:
                    # Determine if the item is a file or a directory
                    is_dir = False
                    if item[-1] == "/":
                        # Remove the trailing slash to get the name of the directory
                        item = item[:-1]
                        is_dir = True

                    # Add the item to the current directory
                    path = "/".join(curr_dir + [item])
                    file_system[path] = {"type": "file" if not is_dir else "dir", "children": {}}

                    if not is_dir:
                        # Parse the size of the file
                        size = int(item.split()[0])
                        file_system[path]["size"] = size

# Calculate the total size of each directory
dirs_under_100000 = []

def calculate_total_size(dir_name):"""