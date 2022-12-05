"""To solve this problem, we need to simulate the rearrangement procedure. We can do this by keeping track of the stacks in a list of lists, where each list represents a stack. For example, the initial configuration in the problem statement would be represented as [['Z', 'N'], ['M', 'C', 'D'], ['P']]. Then, to simulate the first step of the rearrangement procedure, we can remove the top element from stack 2 and append it to stack 1, resulting in the following configuration: [['Z', 'N', 'D'], ['M', 'C'], ['P']]. We can continue simulating the rearrangement procedure in this way until it is complete, and then return the top element of each stack as the final configuration.

Here is one possible implementation in Python:

"""
# Read the input from the file "5_input"
with open('5_input') as f:
    input = f.read().strip().split('\n')

# Initialize the stacks as a list of lists, where each list represents a stack
stacks = [[c for c in stack] for stack in input[0].split()]

# Iterate over the remaining lines of the input, which contain the rearrangement steps
for step in input[1:]:
    # Parse the step to extract the source and destination stacks
    source, _, dest, _, _ = step.split()
    # Convert the stack indices from strings to integers
    source, dest = int(source), int(dest)
    # Remove the top element from the source stack and append it to the destination stack
    stacks[dest-1].append(stacks[source-1].pop())

# Print the top element of each stack as the final configuration
for stack in stacks:
    print(stack[-1], end='')
"""

To use this code, save it in a file called "solution.py" and run it with `python solution.py`. This will print the final configuration of the stacks."""