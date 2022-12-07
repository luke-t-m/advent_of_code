"""To solve this problem, we need to first understand the structure of the file system. The file system is a tree where directories can contain other directories and files. The outermost directory is called `/`.

We can navigate around the file system by changing directory (`cd`) and listing the contents of the current directory (`ls`). When we change directory, we can either move one level down (`cd x`) or one level up (`cd ..`). We can also move to the outermost directory (`cd /`). When we list the contents of the current directory, we can see the files and directories contained by it.

Given the commands and output in the example, we can determine that the file system looks like this:

"""
/ (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
"""

Now, we need to find the directories with a total size of at most 100000 and calculate the sum of their total sizes. In the example above, the directories with a total size of at most 100000 are `a` and `e`. The sum of their total sizes is 95437 (94853 + 584).

To solve this problem, we can first parse the input file and build the file system tree. We can then traverse the tree and calculate the total size of each directory. Finally, we can find the directories with a total size of at most 100000 and calculate the sum of their total sizes.

Here is one possible solution in Python:

"""
# Parse the input file and build the file system tree
with open("7_input") as f:
    lines = f.read().strip().split("\n")

# Helper function to create a new directory
def new_dir(name):
    return {"name": name, "type": "dir", "size": 0, "children": {}}

# Helper function to create a new file
def new_file(name, size):
    return {"name": name, "type": "file", "size": size}

# The root directory
root = new_dir("/")

# The current directory
curr = root

for line in lines:
    # Split the line into tokens
    tokens = line.split()
    
    # If the line is a command
    if tokens[0] == "$":
        # Get the command and arguments
        cmd = tokens[1]
        args = tokens[2:]

        # If the command is "cd"
        if cmd == "cd":
            # If the argument is "..", move up one level
            if args[0] == "..":
                curr = curr["parent"]
            # If the argument is "/", move to the root directory
            elif args[0] == "/":
               """