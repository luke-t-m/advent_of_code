"""The first thing we need to do is parse the input. The input consists of a series of lines, each of which represents a move to be made. A move is specified by the number of crates to move, the stack to move them from, and the stack to move them to. For example, the string `'1 from 2 to 1'` represents moving one crate from stack 2 to stack 1.

To parse the input, we can use the `split` method of the `str` class to split each line into a list of words. Then, we can use the `int` function to convert the numbers in the list to integers. Finally, we can use a regular expression to extract the numbers from the list and store them in variables. Here is an example:

"""
import re

# The input string
line = '1 from 2 to 1'

# Split the string into a list of words
words = line.split(' ')

# Use a regular expression to extract the numbers from the list
# and store them in variables
match = re.match(r'(\d+) from (\d+) to (\d+)', ' '.join(words))
num_crates, from_stack, to_stack = map(int, match.groups())

# Print the variables
print(num_crates)  # 1
print(from_stack)  # 2
print(to_stack)    # 1
"""

Now that we know how to parse the input, let's write a function to do it. The function will take a string as input and return a list of tuples, where each tuple represents a move to be made. The first element of the tuple will be the number of crates to move, and the second and third elements will be the stacks to move them from and to, respectively. Here is the code:

"""
import re

def parse_input(input_str):
    # Split the input string into a list of lines
    lines = input_str.strip().split('\n')

    # Initialize a list to store the moves
    moves = []

    # Loop over the lines
    for line in lines:
        # Split the line into a list of words
        words = line.split(' ')

        # Use a regular expression to extract the numbers from the list
        # and store them in variables
        match = re.match(r'(\d+) from (\d+) to (\d+)', ' '.join(words))
        num_crates, from_stack, to_stack = map(int, match.groups())

        # Append the move to the list
        moves.append((num_crates, from_stack, to_stack))

    return moves

# Test the function
input_str = """1 from 2 to 1
3 from 1 to 3
2 from 2 to 1
1 from 1 to 2"""
print(parse_input(input_str))  # [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
"""

Next, we need to simulate the moves and track the crates as they are moved from one stack to another. To do this, we can use a list to represent the stacks of crates. Each element of the list will be a stack, and each stack will be a list of crates. For example, the stacks from the example in the problem description can be represented as follows:

"""