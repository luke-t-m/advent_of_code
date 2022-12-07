"""First, we need to parse the input to extract the information about the directories and files. We will use a dictionary to store the directories and their contents. The keys of the dictionary will be the names of the directories, and the values will be the sizes of the files in the directory and a list of the directories and files it contains. We will also need a list to store the commands we execute. Here is how we can parse the input and store the information in the dictionary and the list:

"""
# Parse the input
directories = {}
commands = []
current_dir = "/"
with open("7_input") as f:
    for line in f:
        line = line.strip()
        if line.startswith("$"):
            # This line is a command, store it in the list of commands
            commands.append(line[1:].strip())
        else:
            # This line is a file or directory, store it in the current directory
            items = line.split()
            if items[0] == "dir":
                # This is a directory, store it in the dictionary
                directories[current_dir][items[1]] = {"size": 0, "items": {}}
            else:
                # This is a file, store its size in the dictionary
                directories[current_dir][items[1]] = int(items[0])

"""

Next, we need to execute the commands stored in the list of commands. We can do this by iterating over the list of commands and executing each one. If the command is "cd", we need to update the current directory accordingly. If the command is "ls", we can ignore it since we already have all the information about the directories and files. Here is how we can execute the commands:

"""
# Execute the commands
for command in commands:
    if command == "cd /":
        # Go to the outermost directory
        current_dir = "/"
    elif command == "cd ..":
        # Go to the parent directory
        current_dir = "/".join(current_dir.split("/")[:-1])
    elif command.startswith("cd"):
        # Go to a child directory
        current_dir = f"{current_dir}/{command.split()[1]}"

"""

Finally, we need to find all the directories with a total size of at most 100000 and calculate the sum of their total sizes. To do this, we can write a recursive function that takes a directory as input, calculates its total size, and then recursively calls itself on all the directories and files in the directory. The base case of the recursion is when we reach a file, in which case we simply return its size. Here is how we can find the directories with a total size of at most 100000 and calculate the sum of their total sizes:

"""
# Calculate the total size of a directory
def total_size(dir):
    total = 0
    for name, info in dir.items():
        if isinstance(info, int):
            # This is a file, add its size to the total
            total += info
        else:
            # This is a directory, recursively calculate its total size
            total += total_size(info["items"])
    return total

# Find all directories with a total size of at most 100000
directories_under_100000"""