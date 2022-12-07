"""To solve this problem, we will first read the input from the file 7_input and parse it to create a dictionary that represents the file system tree. We will then traverse the tree to calculate the total size of each directory. Finally, we will print the sum of the total sizes of all directories with a size of at most 100000.

Here is a possible solution in Python:

"""
# Parse the input to create a dictionary representing the file system tree
file_system = {}
with open('7_input') as f:
    current_dir = file_system
    for line in f:
        line = line.strip()
        if line.startswith('$'):
            cmd, *args = line[1:].split()
            if cmd == 'cd':
                if args[0] == '/':
                    current_dir = file_system
                elif args[0] == '..':
                    current_dir = list(current_dir.values())[0]
                else:
                    if args[0] not in current_dir:
                        current_dir[args[0]] = {}
                    current_dir = current_dir[args[0]]
        else:
            name, size = line.split()
            current_dir[name] = int(size)

# Traverse the file system tree and calculate the total size of each directory
def calculate_total_size(dir, file_system):
    total_size = 0
    for name, value in file_system[dir].items():
        if type(value) == int:
            total_size += value
        else:
            total_size += calculate_total_size(name, file_system)
    return total_size

# Print the sum of the total sizes of all directories with a size of at most 100000
result = 0
for name, value in file_system.items():
    total_size = calculate_total_size(name, file_system)
    if total_size <= 100000:
        result += total_size
print(result)
""""""