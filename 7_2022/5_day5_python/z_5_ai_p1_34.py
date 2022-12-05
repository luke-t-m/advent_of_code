"""The following is a solution to the given problem written in Python.

"""
def top_of_stacks(input_lines):
    stacks = [[] for _ in range(3)]
    for line in input_lines:
        # Parse the input line.
        words = line.split()
        if words[0] == "move":
            # This is a move instruction.
            _, num_crates, _, _, _, from_stack, _, _, _, to_stack = words
            num_crates = int(num_crates)
            from_stack = int(from_stack[1])
            to_stack = int(to_stack[1])

            # Move the crates.
            crates = stacks[from_stack - 1][-num_crates:]
            stacks[from_stack - 1] = stacks[from_stack - 1][:-num_crates]
            stacks[to_stack - 1].extend(crates)
        else:
            # This is a stack configuration.
            for i, stack in enumerate(words):
                stacks[i].extend(stack[1:-1])

    # Return the top crate in each stack.
    return "".join(stack[-1] for stack in stacks)

# Read the input.
with open("5_input") as file:
    input_lines = file.read().strip().split("\n")

# Solve the problem and print the answer.
print(top_of_stacks(input_lines))
""""""