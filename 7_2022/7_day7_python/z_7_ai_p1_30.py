"""To solve this problem, we need to simulate the directory structure and calculate the total size of each directory.

First, we need to parse the input to extract the commands and the results. We can do this by splitting the input on the `$` character and then splitting each command on the ` ` character to extract the command and its arguments.

Then, we can use a dictionary to store the directory structure. The keys of the dictionary will be the directory names, and the values will be a tuple containing a dictionary for the files and directories contained in that directory, and the total size of the files contained in that directory.

Next, we can iterate over the extracted commands and use them to modify the directory structure. For the `cd` command, we simply need to update the current directory by moving into the specified directory or moving out a level. For the `ls` command, we can add the files and directories listed to the current directory's dictionary.

Finally, we can iterate over the directories and calculate their total sizes by summing the sizes of their files and the total sizes of their subdirectories. We can then find all the directories with a total size of at most 100000 and calculate the sum of their sizes.

Here is an implementation of this approach:

"""
import re

# Parse the input
commands = re.split(r"\$", open("7_input").read().strip())
commands = [(c.split()[0], c.split()[1:]) for c in commands]

# Set up the initial directory structure
dirs = {"/": ({}, 0)}
current_dir = "/"

# Simulate the filesystem
for command, args in commands:
    if command == "cd":
        # Move into or out of the current directory
        if args[0] == "..":
            current_dir = "/".join(current_dir.split("/")[:-1])
        elif args[0] == "/":
            current_dir = "/"
        else:
            current_dir += f"/{args[0]}"
    elif command == "ls":
        # Add the listed files and directories to the current directory
        for item in args:
            if item.startswith("dir"):
                dirs[current_dir][0][item.split()[1]] = ({}, 0)
            else:
                dirs[current_dir][0][item.split()[1]] = int(item.split()[0])

# Calculate the total size of each directory
for dir_name, (dir_content, _) in dirs.items():
    for item_name, item in dir_content.items():
        if type(item) == int:
            dirs[dir_name][1] += item
        else:
            dirs[dir_name][1] += dirs[f"{dir_name}/{item_name}"][1]

# Find the directories with a total size of at most 100000 and calculate the sum of their sizes
total_size = 0
for dir_name, (_, size) in dirs.items():
    if size <= 100000:
        total_size += size

print(total_size)
"""

This code should print the correct answer to the problem."""