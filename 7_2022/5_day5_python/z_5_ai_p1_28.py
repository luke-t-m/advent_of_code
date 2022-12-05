"""To solve this problem, we can simulate the procedure given in the input by using a dictionary to represent the stacks of crates. The keys of the dictionary will represent the stack numbers, and the values will be lists representing the crates in each stack. We will start by reading the input from the file called `5_input`.

First, we define the `main` function and read the input from the file:
"""
def main():
    with open('5_input') as f:
        lines = f.readlines()
"""

Next, we initialize the dictionary of stacks and populate it with the starting positions of the crates. We can do this by splitting each line of the input on the whitespace characters and storing the resulting list of strings as the value for the corresponding stack number in the dictionary.
"""
def main():
    with open('5_input') as f:
        lines = f.readlines()

    stacks = {}
    for line in lines:
        stack_num, *crates = line.split()
        stack_num = int(stack_num[:-1])
        stacks[stack_num] = crates
"""

Now that we have the starting positions of the crates stored in a dictionary, we can simulate the rearrangement procedure. We can do this by looping over the lines of the input, splitting each line on the whitespace characters, and using the resulting values to move crates from one stack to another.
"""
def main():
    with open('5_input') as f:
        lines = f.readlines()

    stacks = {}
    for line in lines:
        stack_num, *crates = line.split()
        stack_num = int(stack_num[:-1])
        stacks[stack_num] = crates

    for line in lines:
        _, num_crates, _, from_stack, _, _, _, _, _, _, to_stack = line.split()
        num_crates = int(num_crates)
        from_stack = int(from_stack)
        to_stack = int(to_stack)

        crates = stacks[from_stack][-num_crates:]
        stacks[from_stack] = stacks[from_stack][:-num_crates]
        stacks[to_stack].extend(crates)
"""

Finally, we can print the top crate in each stack by accessing the first element of each list in the dictionary.
"""
def main():
    with open('5_input') as f:
        lines = f.readlines()

    stacks = {}
    for line in lines:
        stack_num, *crates = line.split()
        stack_num = int(stack_num[:-1])
        stacks[stack_num] = crates

    for line in lines:
        _, num_crates, _, from_stack, _, _, _, _, _, _, to_stack = line.split()
        num_crates = int(num_crates)
        from_stack = int(from_stack)
        to_stack = int(to_stack)

        crates = stacks[from_stack][-num_crates:]
        stacks[from_stack] = stacks[from_stack][:-num_crates]
        stacks[to_stack].extend(crates)

    for"""