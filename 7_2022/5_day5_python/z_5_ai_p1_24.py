"""The code to solve the problem is as follows:

"""
# read input
with open("5_input") as f:
    lines = f.readlines()

# initialize stacks
stacks = [list(line.strip()) for line in lines]

# parse instructions
instructions = []
for line in lines[1:]:
    words = line.split()
    num_crates = int(words[1])
    src_stack = int(words[3])
    dest_stack = int(words[5])
    instructions.append((num_crates, src_stack, dest_stack))

# apply instructions
for num_crates, src_stack, dest_stack in instructions:
    crates = [stacks[src_stack-1].pop() for _ in range(num_crates)]
    stacks[dest_stack-1].extend(crates)

# print top crates of each stack
print("".join(stacks[i][-1] for i in range(len(stacks))))
"""

The code works as follows:

1. Read the input from the `5_input` file.
2. Initialize the stacks based on the input.
3. Parse the instructions from the input.
4. Apply the instructions to the stacks by moving the specified number of crates from the source stack to the destination stack.
5. Print the top crates of each stack."""