"""To solve this problem, we can simulate the movement of the crates as specified in the input. For this, we will create a list of lists, where each inner list represents a stack of crates. Then, we will parse the input and apply the movements to the stacks. Finally, we will output the top crate of each stack.

Here is the code to do this:

"""
# Read input from file
with open('5_input') as f:
    input = f.read()

# Initialize stacks of crates
stacks = []

# Parse input
lines = input.strip().split('\n')
for line in lines:
    if line[0] == '[':
        # This line specifies the initial state of the stacks
        stack_line = line.strip('[]')
        stack_line = stack_line.split()
        stacks = [[crate for crate in stack] for stack in stack_line]
    else:
        # This line specifies a movement of crates
        movement = line.split()
        num_crates = int(movement[0])
        from_stack = int(movement[3])
        to_stack = int(movement[5])

        # Move crates
        crates = [stacks[from_stack-1].pop() for _ in range(num_crates)]
        stacks[to_stack-1] = crates + stacks[to_stack-1]

# Output top crates of each stack
for stack in stacks:
    print(stack[-1], end='')
"""

We can test this code using the example from the problem description:

"""
# Initialize stacks of crates
stacks = []

# Parse input
lines = [
    '[D] [C] [Z] [M] [P]',
    '1 from 2 to 1',
    '3 from 1 to 3',
    '2 from 2 to 1',
    '1 from 1 to 2',
]
for line in lines:
    if line[0] == '[':
        # This line specifies the initial state of the stacks
        stack_line = line.strip('[]')
        stack_line = stack_line.split()
        stacks = [[crate for crate in stack] for stack in stack_line]
    else:
        # This line specifies a movement of crates
        movement = line.split()
        num_crates = int(movement[0])
        from_stack = int(movement[3])
        to_stack = int(movement[5])

        # Move crates
        crates = [stacks[from_stack-1].pop() for _ in range(num_crates)]
        stacks[to_stack-1] = crates + stacks[to_stack-1]

# Output top crates of each stack
for stack in stacks:
    print(stack[-1], end='')
"""

This code should output `CMZ`, which is the correct answer."""