"""To solve this problem, we will first define a few functions. The first function will take a string representing the state of the stacks and return a list of the stacks. For example, the string `"[D] [N] [C]\n[Z] [M] [P]\n 1   2   3"` would be parsed into the list `[["D", "N", "C"], ["Z", "M", "P"], ["1", "2", "3"]]`.

The second function will take a list of the stacks and a string representing a move and update the list of stacks accordingly. For example, if the input is `[["D", "N", "C"], ["Z", "M", "P"], ["1", "2", "3"]]` and the move is `"move 2 from 3 to 1"`, the function will return the updated list of stacks `[["D", "N", "C", "2"], ["Z", "M", "P"], ["1", "3"]]`.

The third function will take a list of the stacks and return a string representing the state of the stacks. This is the reverse of the first function. For example, the input `[["D", "N", "C"], ["Z", "M", "P"], ["1", "2", "3"]]` would return the string `"[D] [N] [C]\n[Z] [M] [P]\n 1   2   3"`.

We can then use these functions to solve the problem as follows:
1. Read the input from the file `5_input`. The input will contain the initial state of the stacks followed by a series of moves.
2. Use the first function to parse the input into a list of the stacks.
3. Iterate over the moves and use the second function to update the list of stacks.
4. Use the third function to format the final list of stacks into a string.
5. Print the final string.

Here is a possible implementation of the solution in Python:

"""
def parse_stacks(s):
    # split the string into lines
    lines = s.strip().split("\n")
    # split the lines into stacks
    stacks = [list(line) for line in lines[:-1]]
    # return the stacks
    return stacks

def move(stacks, move):
    # split the move string into words
    words = move.split()
    # extract the number of crates to move
    num_crates = int(words[1])
    # extract the source and destination stack indices
    src = int(words[2][:-2])
    dest = int(words[-1])
    # move the crates from the source stack to the destination stack
    for _ in range(num_crates):
        stacks[dest - 1].append(stacks[src - 1].pop())
    # return the updated stacks
    return stacks

def format_stacks(stacks):
    # create a list of strings representing the stacks
    stack_strings = ["".join(stack) for stack in stacks]
    # create a string representing the stacks
    s = "\n".join(stack_strings)
    # add the numbers below the stacks
    s += "\n" + "   ".join(str(i) for i in range(1, len(stacks) + 1))
    # return the formatted string