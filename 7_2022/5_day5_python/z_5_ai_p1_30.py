"""The solution to this problem is as follows:

1. Read the input file `5_input` and store it in a list of strings.
2. Iterate over each string in the list, and for each string, split it into a list of words.
3. Parse the list of words to get the relevant information, namely the source stack, the destination stack, and the number of crates to move.
4. Use this information to move the crates in the stacks, one at a time.
5. After all the moves are completed, print the top crate of each stack.

Here is the implementation in Python:

"""
# Read the input file and store it in a list of strings
with open('5_input', 'r') as f:
    lines = f.readlines()

# Initialize the stacks
stacks = [[], [], []]

# Iterate over each line in the input
for line in lines:
    # Split the line into a list of words
    words = line.split()

    # Get the source and destination stacks and the number of crates
    src = int(words[1]) - 1  # subtract 1 because stacks are 0-indexed
    dest = int(words[3]) - 1
    num_crates = int(words[4])

    # Move the crates one at a time
    for _ in range(num_crates):
        # Take the top crate from the source stack
        crate = stacks[src].pop()

        # Put the crate on top of the destination stack
        stacks[dest].append(crate)

# Print the top crate of each stack
for i, stack in enumerate(stacks):
    print(f'Top crate on stack {i+1}: {stack[-1]}')
""""""