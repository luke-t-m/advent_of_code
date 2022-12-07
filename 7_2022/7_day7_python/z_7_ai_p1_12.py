"""You can solve this problem in Python by using a combination of regular expressions, recursion, and dictionaries.

First, you will need to read in the input from the file `7_input`. You can do this using the `open` and `readlines` functions. This will give you a list of strings, each representing a line of input from the file.

Next, you can use a regular expression to parse the input and extract the relevant information from each line. Specifically, you will want to use a regular expression that can match lines that begin with `cd`, `ls`, or `$`.

For lines that begin with `cd`, you will want to extract the directory name that is being changed to. For lines that begin with `ls`, you will want to extract the list of files and directories in the current directory. For lines that begin with `$`, you will want to extract the command that was executed.

Once you have extracted this information from the input, you can use a recursive function to traverse the file system and compute the total size of each directory. This function should take as input the current directory and a dictionary that maps directory names to their total sizes.

The function should start by adding the size of all the files in the current directory to the total size of the directory. Then, it should loop through the list of directories and files in the current directory and recursively call itself on each directory. After all of the recursive calls have completed, the function should return the total size of the current directory.

Finally, you can use a loop to sum up the total size of all directories with a total size of at most 100000, and print the result.

Here is an example implementation of this solution in Python:

"""
import re

# Read input from file
with open('7_input', 'r') as f:
  input = f.readlines()

# Parse input using regular expressions
commands = []
for line in input:
  # Match lines that begin with cd
  match = re.match(r'cd (.*)', line)
  if match:
    # Extract the directory name and add it to the list of commands
    commands.append(('cd', match.group(1)))
    continue

  # Match lines that begin with ls
  match = re.match(r'ls (.*)', line)
  if match:
    # Extract the list of files and directories and add it to the list of commands
    commands.append(('ls', match.group(1).split()))
    continue

  # Match lines that begin with $
  match = re.match(r'\$ (.*)', line)
  if match:
    # Extract the command and add it to the list of commands
    commands.append(('$', match.group(1)))

# Recursive function to compute total size of a directory
def compute_size(dir, sizes):
  # Add the size of all the files in the current directory to the total size
  for file in commands[dir][1]:
    # If the file is a number, it is a file size
    if file.isnumeric():
      sizes[commands[dir][0]] += int(file)

  # Recursively compute the size of each subdirectory
  for file in commands[dir][1]:
    # If the file is not a number, it is a directory
    if not file.isnumeric():
      # If the directory has not"""