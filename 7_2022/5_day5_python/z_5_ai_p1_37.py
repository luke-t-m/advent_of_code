"""To solve this problem, you will need to implement a function that takes as input a description of the initial state of the crates, and a series of instructions for how to rearrange the crates, and then return the letters of the crates that end up on top of each stack.

Here is an example of how your function could be used:

"""
# Read the input from the file 5_input
with open("5_input") as f:
    input_str = f.read()

# Parse the input and extract the initial state of the crates and the rearrangement instructions
initial_state, instructions = parse_input(input_str)

# Solve the problem
result = solve(initial_state, instructions)

# Print the result
print(result)
"""

You will need to implement the `parse_input()` and `solve()` functions. The `parse_input()` function should take the input string as input and return a tuple containing the initial state of the crates and the instructions for how to rearrange them. The `solve()` function should take the initial state and instructions as input and return the letters of the crates that end up on top of each stack.

The initial state of the crates is given as a list of strings, where each string represents a stack of crates. The first character of each string is the letter of the crate on the top of the stack, and the last character is the letter of the crate on the bottom of the stack. For example, the initial state `["ZN", "MCD", "P"]` means that there are three stacks of crates, and the crates in each stack are as follows:

* Stack 1: Z (top), N (bottom)
* Stack 2: M (bottom), C (middle), D (top)
* Stack 3: P (top)

The rearrangement instructions are given as a list of strings, where each string has the following format: `"move x from y to z"`. This means that x crates should be moved from stack y to stack z, with the top crate being moved first. For example, the instruction `"move 1 from 2 to 1"` means that one crate should be moved from stack 2 to stack 1, with the top crate being moved first.

To solve the problem, you will need to simulate the rearrangement of the crates according to the given instructions. At each step of the simulation, you should move the specified number of crates from one stack to another, starting with the top crate of the source stack. When moving a crate from one stack to another, you should add it to the top of the destination stack. When a stack becomes empty, you should remove it from the list of stacks.

After all of the instructions have been applied, you should return the letters of the crates that are on top of each stack, in the order in which the stacks appear in the input. For example, if the initial state is `["ZN", "MCD", "P"]` and the instructions are `["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"]`, then the final state of the crates is `["CD", "MN", "ZP"]`, and the function should return the string `"CDZP"`.

You can assume that the input is always valid, and that the instructions will always be valid for the given initial state of the crates. You do not need to worry about the case where a stack becomes empty before all"""