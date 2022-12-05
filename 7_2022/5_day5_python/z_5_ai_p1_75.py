"""To solve this problem, we will first read in the initial crate stack configuration from the `5_input` file. We will then apply the steps of the rearrangement procedure one at a time, updating the stack configuration after each step. Finally, we will print the top crate on each stack.

Here is one way to solve this problem in Python:

"""
# Read in the initial stack configuration
with open("5_input") as f:
    lines = f.read().strip().split("\n")

# Parse the stack configuration
stacks = []
for line in lines[:-1]:
    stack = []
    for c in line:
        if c.isalpha():
            stack.append(c)
    stacks.append(stack)

# Parse the rearrangement steps
steps = []
for step in lines[-1:]:
    words = step.split()
    move = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5])
    steps.append((move, from_stack, to_stack))

# Apply the rearrangement steps
for move, from_stack, to_stack in steps:
    # Remove the top `move` crates from the `from_stack`
    crates = stacks[from_stack - 1][-move:]
    stacks[from_stack - 1] = stacks[from_stack - 1][:-move]

    # Add the removed crates to the top of the `to_stack`
    stacks[to_stack - 1].extend(crates)

# Print the top crate on each stack
for stack in stacks:
    print(stack[-1], end="")
"""

We can save this code to a file called `solution.py` and run it with the following command to solve the problem and print the answer:

"""
python solution.py
""""""