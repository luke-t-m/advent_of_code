"""First, we need to parse the input to extract the filesystem data. The file is formatted as a sequence of lines, each corresponding to either a command or its output. We can represent each file as a dictionary with two keys: 'type' and 'size', where 'type' is either 'dir' or 'file' and 'size' is an integer representing the size of the file if it is a file. We can represent the entire filesystem as a dictionary of dictionaries, where the keys are file/directory names and the values are the corresponding file/directory data.

To parse the input, we can iterate over the lines in the input file and use a stack to keep track of the current directory. Whenever we encounter a 'cd' command, we update the current directory by pushing or popping from the stack depending on the argument to the 'cd' command. Whenever we encounter an 'ls' command, we add the listed files/directories to the current directory.

Once we have parsed the input and built the filesystem representation, we can use a recursive function to compute the total size of each directory. This function takes a directory as input and returns the total size of the directory by adding the sizes of all of the files and directories it contains, directly or indirectly.

We can then find all of the directories with a total size of at most 100000 by iterating over the keys in the filesystem dictionary and calling the total size function on each directory. We can then sum the sizes of these directories and print the result.

Here is the code:

"""
import re


def parse_input(input_str):
    # Parse the input and return the filesystem representation
    lines = input_str.strip().split('\n')
    filesystem = {}
    curr_dir = ['']  # Stack of directories, starting with the root directory

    for line in lines:
        if line.startswith('$'):
            # Parse command
            m = re.match(r'^\$ (cd|ls) (.*)', line)
            cmd, arg = m.groups()

            if cmd == 'cd':
                if arg == '/':
                    # Switch to root directory
                    curr_dir = ['']
                elif arg == '..':
                    # Go up one level
                    curr_dir.pop()
                else:
                    # Go down one level
                    curr_dir.append(arg)
        else:
            # Parse 'ls' output
            items = line.strip().split()
            for item in items:
                m = re.match(r'^(\d+)\s+(\S+)$', item)
                size, name = m.groups()
                size = int(size)

                # Add file/directory to current directory
                curr_path = '/'.join(curr_dir)
                curr_dir_data = filesystem.setdefault(curr_path, {})
                curr_dir_data[name] = {'type': 'file', 'size': size}

    return filesystem


def total_size(filesystem, path):
    # Return the total size of the directory at the given path
    dir_data = filesystem[path]
    size = 0

    for name, file_data in dir_data.items():
        if file_data['type'] == 'file':
            size += file_data['size']
        else:
            # Recurs"""