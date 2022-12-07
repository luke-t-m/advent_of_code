"""# This function receives the output of the terminal in the form of a list of strings, where each string is a line of the output
# It returns the sum of the sizes of all directories that have a total size of at most 100000
def solve(output: List[str]) -> int:
    # The current directory is / initially
    current_dir = "/"
    # The size of each directory is stored in this dictionary
    dir_sizes = {}
    # We keep track of the directories that are ancestors of the current directory in a list
    # So if the current directory is /a/b/c, the list would be ["/", "a", "b", "c"]
    # This is used to find the parent directory of the current directory using the "cd .." command
    ancestor_dirs = ["/"]
    
    # We iterate over each line of the output
    for line in output:
        # We split the line by space to separate the command and its arguments
        split_line = line.split(" ")
        # If the line is a command, we process it
        if line[0] == "$":
            # If the command is "cd", we change the current directory
            if split_line[1] == "cd":
                # If the argument is "/", we switch to the outermost directory
                if split_line[2] == "/":
                    current_dir = "/"
                    ancestor_dirs = ["/"]
                # If the argument is "..", we move one directory out
                elif split_line[2] == "..":
                    # We remove the last entry of the ancestor_dirs list, which is the current directory
                    ancestor_dirs.pop()
                    # The new current directory is the last entry of the ancestor_dirs list
                    current_dir = ancestor_dirs[-1]
                # If the argument is a directory name, we move one directory in
                else:
                    # We append the directory name to the current directory to find the new current directory
                    current_dir += "/" + split_line[2]
                    # We append the new current directory to the ancestor_dirs list
                    ancestor_dirs.append(current_dir)
        # If the line is not a command, it is the output of the "ls" command
        else:
            # We split the line by space to separate the size and the name of each file or directory in the current directory
            split_line = line.split(" ")
            # If the line is a directory, we add it to the ancestor_dirs list
            if split_line[0] == "dir":
                ancestor_dirs.append(current_dir + "/" + split_line[1])
            # If the line is a file, we update the size of the current directory
            else:
                # We convert the size of the file from string to integer
                size = int(split_line[0])
                # If the current directory is not in the dir_sizes dictionary, we add it and set its size to 0
                if current_dir not in dir_sizes:
                    dir_sizes[current_dir] = 0
                # We add the size of the file to the size of the current directory
                dir_sizes[current_dir] += size
    
    # We initialize the sum of the sizes of the directories with total size"""