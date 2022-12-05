"""To solve this problem, we can simulate the rearrangement procedure using python code. We will need to read the input from a file called `5_input`. To do this, we can use the `open()` and `readlines()` functions.

First, we will initialize a list `stacks` to represent the stacks of crates. We will also initialize a list `top_crates` to store the top crates of each stack after the rearrangement procedure is complete. Then, we will read the input from the file, line by line. For each line in the input, we will split the line into tokens using the `split()` function. If the line contains the string "move", then we will move the specified number of crates from one stack to another. Otherwise, we will add the crates in the line to the corresponding stack.

After we have processed all of the lines in the input, we will loop through the stacks and add the top crate of each stack to `top_crates`. Then, we will print `top_crates` to get the answer.

Here is the code:

"""
# Initialize the stacks and top crates lists
stacks = []
top_crates = []

# Open the input file and read the lines
with open("5_input") as f:
    lines = f.readlines()

# Loop through the lines in the input
for line in lines:
    # Split the line into tokens
    tokens = line.split()

    # If the line contains the string "move", move the specified number of crates
    if "move" in line:
        # Get the number of crates to move and the source and destination stacks
        num_crates = int(tokens[1])
        src_stack = int(tokens[2])
        dest_stack = int(tokens[5])

        # Move the crates from the source stack to the destination stack
        for _ in range(num_crates):
            crate = stacks[src_stack - 1].pop()
            stacks[dest_stack - 1].append(crate)
    else:
        # Add the crates in the line to the corresponding stack
        stack_num = int(tokens[0])
        crates = tokens[1:]
        stacks.append(crates)

# Loop through the stacks and add the top crate of each stack to top_crates
for stack in stacks:
    top_crates.append(stack[-1])

# Print the top crates of each stack
print(top_crates)
""""""