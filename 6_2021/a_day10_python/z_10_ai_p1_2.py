"""You can use a stack to keep track of the open brackets as you iterate through the line. When you encounter a closing bracket, pop the top item from the stack and check if it matches the closing bracket. If it does not match, the line is corrupted. To calculate the score, use a dictionary to map each illegal character to its corresponding score.

Here is a possible solution in Python:

"""
# Read the input from a file called 10_input
with open("10_input") as f:
    lines = f.read().strip().split("\n")

# Map each illegal character to its corresponding score
score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}

# Iterate through each line
for line in lines:
    # Keep track of the open brackets in a stack
    stack = []

    # Iterate through each character in the line
    for char in line:
        # If the character is an open bracket, append it to the stack
        if char in "([{<":
            stack.append(char)
        # If the character is a closing bracket, check if it matches the top item in the stack
        elif char in ")]}>":
            # If the stack is empty or the top item does not match the closing bracket, the line is corrupted
            if not stack or char != stack.pop():
                # Print the score and break out of the inner loop
                print(score_map[char])
                break
    # If the stack is not empty, the line is corrupted
    else:
        if stack:
            print(score_map[stack.pop()])