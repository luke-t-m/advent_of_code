"""To solve this problem, we need to simulate the rearrangement procedure. We can do this by creating a list of lists, where each list represents a stack. In each step of the rearrangement procedure, we will take the crates from the specified stack and move them to the specified destination stack.

To start, we need to read in the initial state of the stacks from the input file. We can do this by reading each line of the file and splitting it on the space character. This will give us a list of strings, which we can then convert to a list of lists of strings, where each string is a crate.

We can then loop through the remaining lines in the input file and split each line on the space character to extract the instructions for each step of the rearrangement procedure. We can then use the instructions to move the crates from one stack to another.

Finally, we can loop through the list of stacks and print the top crate in each stack to get the final arrangement of crates.

Here is the code:

"""
# Read in the initial state of the stacks from the input file
with open('5_input') as f:
    stacks = [list(line.strip()) for line in f]

# Loop through the remaining lines in the input file
for line in f:
    # Split the line on the space character to extract the instructions
    # for this step of the rearrangement procedure
    src, _, dest = line.split()
    # Convert the source and destination stack indices to integers
    src = int(src)
    dest = int(dest)
    # Move the top crate from the source stack to the destination stack
    stacks[dest].append(stacks[src].pop())

# Loop through the stacks and print the top crate in each stack
for stack in stacks:
    print(stack[-1], end='')
""""""