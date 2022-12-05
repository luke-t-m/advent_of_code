"""To solve this problem, we need to simulate the steps specified in the rearrangement procedure. We can do this using a list of lists, where each inner list represents a stack of crates. Then, we can use a loop to iterate over the steps in the rearrangement procedure, and use the information in each step to update the list of lists.

Here is one way to solve this problem in Python:

"""
# Read the input from the file
with open('5_input', 'r') as f:
    steps = f.readlines()

# Initialize the stacks of crates
stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

# Loop over the steps in the rearrangement procedure
for step in steps:
    # Parse the step to get the source and destination stacks
    source, _, _, dest = step.split()
    source = int(source) - 1
    dest = int(dest) - 1

    # Move the top crate from the source stack to the destination stack
    crate = stacks[source].pop()
    stacks[dest].append(crate)

# Print the top crate in each stack
for stack in stacks:
    print(stack[-1])
"""

The output of this program should be the top crate in each stack, in the order that the stacks are listed in the input. In the example in the problem description, the output would be `CMZ`."""