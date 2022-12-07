"""To solve this problem, we will use a recursive function that traverses the directories and files of the filesystem. This function will take as input the current directory, a dictionary containing the visited directories and their sizes, and a list containing the directories with total size of at most 100000. The function will return the sum of the sizes of the directories with total size of at most 100000.

First, we need to parse the input from the file and store it in a dictionary containing the directories and their contents. This dictionary will have the following format:
"""
{
    "dir1": {
        "dir2": {
            "file1": 123,
            "file2": 456
        },
        "file3": 789
    }
}
"""
This means that the directory "dir1" contains the directory "dir2" and the file "file3". The directory "dir2" contains the files "file1" and "file2".

We will use the `re.findall()` function to parse the input and extract the commands and the resulting outputs. Then, we will iterate over the commands and outputs and update the dictionary accordingly.

Here is the code to parse the input and store it in the dictionary:

"""
import re

# Read input from file
with open("7_input", "r") as f:
    input_lines = f.read().strip().split("\n")

# Parse input
commands = []
outputs = []
for line in input_lines:
    if line.startswith("$"):
        commands.append(line[1:].strip())
    else:
        outputs.append(line.strip())

# Initialize dictionary
filesystem = {}

# Iterate over commands and outputs
i = 0
while i < len(commands):
    # Get current directory
    cur_dir = filesystem
    dirs = ["/"]
    while len(dirs) > 0:
        d = dirs.pop(0)
        if d in cur_dir:
            cur_dir = cur_dir[d]
        else:
            cur_dir[d] = {}
            cur_dir = cur_dir[d]
    # Parse and execute command
    command = commands[i].split()
    if command[0] == "cd":
        # Change directory
        if command[1] == "/":
            # Go to outermost directory
            dirs = ["/"]
        elif command[1] == "..":
            # Go to parent directory
            dirs = dirs[:-1]
        else:
            # Go to subdirectory
            dirs.append(command[1])
    elif command[0] == "ls":
        # List contents of current directory
        output = outputs[i].split()
        j = 0
        while j < len(output):
            # Parse output
            if output[j] == "dir":
                # Directory
                j += 1
                cur_dir[output[j]] = {}
            else:
                # File
                size = int(output[j])
                j += 1
                name = output[j]
                cur_dir[name] = size
            j += 1
    i += 1
"""

Now that we have parsed the input and stored it in the dictionary, we can implement"""