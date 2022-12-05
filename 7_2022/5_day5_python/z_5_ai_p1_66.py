"""To solve this problem, we can simulate the rearrangement procedure. We can do this by creating a list of lists representing the stacks of crates, and then applying each step of the procedure to the list of stacks.

First, we need to parse the input to get the initial state of the stacks and the list of rearrangement steps. We can do this using a combination of string splitting and list slicing. For example, we can split the input string on the newline character to get a list of lines, and then split each line on the space character to get a list of words. We can then use list slicing to get the relevant parts of the input.

Once we have the initial state of the stacks and the list of rearrangement steps, we can simulate the rearrangement procedure. To do this, we can iterate over the list of steps and apply each step to the list of stacks. We can use list indexing to move crates between stacks, and we can use the `pop()` and `insert()` methods to move crates within a stack.

Finally, we need to print the top crate on each stack. We can do this by iterating over the list of stacks and printing the first element of each stack.

Here is a complete implementation of this solution in Python:

"""
# Parse the input to get the initial state of the stacks and the list of steps
input_str = open("5_input").read()
lines = input_str.split("\n")
stacks = [list(line) for line in lines[:3]]
steps = [tuple(line.split()) for line in lines[3:]]

# Simulate the rearrangement procedure
for step in steps:
    # Get the source and destination stacks
    src_stack = int(step[1]) - 1
    dest_stack = int(step[3]) - 1

    # Move the crates
    num_crates = int(step[0])
    for i in range(num_crates):
        crate = stacks[src_stack].pop()
        stacks[dest_stack].insert(0, crate)

# Print the top crate on each stack
for stack in stacks:
    print(stack[0])
""""""