"""First, we will import the `os` module to be able to use the `walk` function which is used to iterate through the directories and files.
"""
import os
"""

Next, we will define a function called `get_dir_size` that takes a directory as an input and returns the total size of that directory. We will initialize the `size` variable to 0 and iterate through the files and directories in the input directory using the `walk` function.
"""
def get_dir_size(dir):
    size = 0
    for path, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(path, file)
            size += os.path.getsize(file_path)
    return size
"""

Next, we will define the main function that will read the input from the file and print the sum of the total sizes of all directories with total size at most 100000. We will use the `os.walk` function to iterate through the directories and files in the input and call the `get_dir_size` function to calculate the total size of each directory. We will keep a running sum of the total sizes of directories with size at most 100000 and print it at the end.
"""
def main():
    # read the input
    with open('7_input') as f:
        input = f.read().strip().split('\n')

    # initialize the running sum
    sum = 0

    # iterate through the directories and files in the input
    for path, dirs, files in os.walk('/'):
        for dir in dirs:
            # calculate the total size of the directory
            dir_path = os.path.join(path, dir)
            dir_size = get_dir_size(dir_path)

            # add the total size to the running sum if it is at most 100000
            if dir_size <= 100000:
                sum += dir_size

    # print the sum
    print(sum)
"""

Finally, we will call the main function to run the program.
"""
if __name__ == '__main__':
    main()
"""

The complete program is shown below.
"""
import os

def get_dir_size(dir):
    size = 0
    for path, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(path, file)
            size += os.path.getsize(file_path)
    return size

def main():
    # read the input
    with open('7_input') as f:
        input = f.read().strip().split('\n')

    # initialize the running sum
    sum = 0

    # iterate through the directories and files in the input
    for path, dirs, files in os.walk('/'):
        for dir in dirs:
            # calculate the total size of the directory
            dir_path = os.path.join(path, dir)
            dir_size = get_dir_size(dir_path)

            # add the total size to the running sum if it is at most 100000
            if dir_size <= 100000:
                sum += dir_size

    # print the sum
    print("""