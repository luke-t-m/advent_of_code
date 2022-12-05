"""The first thing we need to do is open the input file, which is called "5_input". We will use the open() function to do this.

"""
with open("5_input") as f:
    # read the input data here
"""

Next, we will read the input data from the file. Each line of the file contains a step in the rearrangement procedure. We can use a for loop to iterate over the lines in the file, and split each line on the space character to get the individual elements of the step.

"""
with open("5_input") as f:
    for line in f:
        move_from, _, move_to, _, _ = line.split(" ")
        # process the move here
"""

Now we need to actually perform the moves specified in the input data. We can represent the stacks of crates as a list of lists, where each sublist represents a stack of crates. We will use the move_from and move_to variables to specify which stack to move crates from and to, respectively.

"""
with open("5_input") as f:
    stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    for line in f:
        move_from, _, move_to, _, _ = line.split(" ")
        move_from = int(move_from) - 1
        move_to = int(move_to) - 1
        crates = stacks[move_from].pop()
        stacks[move_to].append(crates)
    # print the top crate in each stack
"""

Finally, we need to print the top crate in each stack after all of the moves have been performed. We can do this by iterating over the stacks and printing the last element of each stack.

"""
with open("5_input") as f:
    stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    for line in f:
        move_from, _, move_to, _, _ = line.split(" ")
        move_from = int(move_from) - 1
        move_to = int(move_to) - 1
        crates = stacks[move_from].pop()
        stacks[move_to].append(crates)
    for stack in stacks:
        print(stack[-1], end="")
"""

Putting it all together, we get the following code:

"""
with open("5_input") as f:
    stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    for line in f:
        move_from, _, move_to, _, _ = line.split(" ")
        move_from = int(move_from) - 1
        move_to = int(move_to) - 1
        crates = stacks[move_from].pop()
        stacks[move_to].append(crates)
    for stack in stacks:
        print(stack[-1], end="")
""""""