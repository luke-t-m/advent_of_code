"""You can solve this problem by traversing the file system and keeping track of the total sizes of the directories. Here's how you could solve this problem in Python:

1. Parse the input to create a list of commands.
2. Create a dictionary that maps directory names to total sizes.
3. Iterate over the list of commands, updating the dictionary as you go.
4. When you encounter a `cd` command, update the current directory.
5. When you encounter an `ls` command, add the size of each file in the current directory to the total size of the current directory.
6. When you encounter a `cd ..` command, move to the parent directory of the current directory.
7. When you encounter a `cd /` command, move to the root directory.
8. At the end of the input, calculate the sum of the total sizes of all directories with a total size of at most 100000.

Here's some example code that demonstrates how you could do this:

"""
# Parse the input to create a list of commands
commands = []
with open("7_input") as f:
    for line in f:
        if line.startswith("$"):
            commands.append(line[2:].strip().split())

# Create a dictionary that maps directory names to total sizes
directories = {"/": 0}
current_dir = "/"

# Iterate over the list of commands, updating the dictionary as you go
for command in commands:
    if command[0] == "cd":
        if command[1] == "..":
            # Move to the parent directory of the current directory
            current_dir = "/".join(current_dir.split("/")[:-1])
        elif command[1] == "/":
            # Move to the root directory
            current_dir = "/"
        else:
            # Update the current directory
            current_dir = current_dir + "/" + command[1]
            if current_dir not in directories:
                directories[current_dir] = 0
    elif command[0] == "ls":
        # Add the size of each file in the current directory to the total size of the current directory
        for i in range(1, len(command), 2):
            if command[i + 1].endswith(".txt") or command[i + 1].endswith(".dat"):
                directories[current_dir] += int(command[i])

# Calculate the sum of the total sizes of all directories with a total size of at most 100000
result = 0
for directory, size in directories.items():
    if size <= 100000:
        result += size

# Print the result
print(result)
""""""