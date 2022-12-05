"""The following is a correct implementation of the solution to the problem in Python.

"""
# read input from file
with open("5_input", "r") as f:
    input_lines = f.readlines()

# parse input
stacks = []
for line in input_lines:
    # split line into list of strings
    crates = line.strip().split()
    # convert each string to integer
    crates = [int(c) for c in crates]
    # append list of crates to list of stacks
    stacks.append(crates)

# apply rearrangement steps
for step in input_lines[3:]:
    # split step into a list of strings
    tokens = step.strip().split()
    # extract the numbers from the step
    a, b, c = [int(t) for t in tokens if t.isdigit()]
    # apply the step
    stacks[b - 1].pop()
    stacks[c - 1].append(a)

# create the message by extracting the top crate from each stack
message = "".join([str(stack[-1]) for stack in stacks])

# print the message
print(message)
""""""