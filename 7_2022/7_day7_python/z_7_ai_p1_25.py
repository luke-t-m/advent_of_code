"""You can solve this problem by creating a class representing a directory and its files. The class should have methods to calculate the total size of the directory and its subdirectories, to add files and directories to the current directory, and to move up and down the directory tree.

Here is an example of how you could implement this class in Python:

"""
class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirectories = []

    def total_size(self):
        total = 0
        for file in self.files:
            total += file.size
        for subdir in self.subdirectories:
            total += subdir.total_size()
        return total

    def add_file(self, file):
        self.files.append(file)

    def add_subdirectory(self, subdir):
        self.subdirectories.append(subdir)

    def move_up(self):
        # move up to the parent directory

    def move_down(self, name):
        # move down to the subdirectory with the given name
"""

Then, you can parse the input file and use this class to navigate the filesystem and calculate the total size of each directory. You can use the `total_size` method to find all directories with a total size of at most 100000 and calculate the sum of their total sizes.

Here is an example of how you could parse the input file and use the `Directory` class to solve the problem:

"""
# parse the input file and create the root directory
root = Directory("/")
current_dir = root
with open("7_input") as f:
    for line in f:
        if line.startswith("$"):
            # this is a command, parse it
            command, *args = line.strip("$").split()
            if command == "cd":
                # change directory
                if args[0] == "..":
                    current_dir = current_dir.move_up()
                elif args[0] == "/":
                    current_dir = root
                else:
                    current_dir = current_dir.move_down(args[0])
            elif command == "ls":
                # list files and directories in the current directory
                for item in args:
                    if item.endswith(".txt") or item.endswith(".dat"):
                        # this is a file, add it to the current directory
                        size, name = item.split()
                        file = File(name, int(size))
                        current_dir.add_file(file)
                    else:
                        # this is a directory, add it to the current directory
                        size, name = item.split()
                        dir = Directory(name)
                        current_dir.add_subdirectory(dir)

# find all directories with a total size of at most 100000
# and calculate the sum of their total sizes
total = 0
for subdir in root.subdirectories:
    if subdir.total_size() <= 100000:
        total += subdir.total_size()
print(total)
""""""