"""The following code will solve the problem. It reads the input from a file called `10_input`, and prints the answer.
"""
# Read the input
with open("10_input", "r") as f:
    lines = f.readlines()

# The maximum score for any syntax error
max_score = 0

# Iterate over each line in the input
for line in lines:
    # The stack of open brackets
    stack = []
    # The current score for the line
    score = 0
    
    # Iterate over each character in the line
    for c in line:
        # If the character is an opening bracket, add it to the stack
        if c in "([{<":
            stack.append(c)
        # If the character is a closing bracket, check if it matches the last opening bracket
        elif c in ")]}>":
            if not stack:
                # If the stack is empty, the line is corrupted and we stop checking
                break
            # If the closing bracket does not match the last opening bracket, the line is corrupted and we stop checking
            elif c != {")": "(", "]": "[", "}": "{", ">": "<"}[c]:
                break
            # If the closing bracket matches the last opening bracket, we remove the last opening bracket from the stack
            else:
                stack.pop()
    
    # If there are any opening brackets left on the stack, the line is corrupted and we ignore it
    if stack:
        continue
    
    # If we reach this point, the line is not corrupted, so we add its syntax error score to the maximum score
    for c in line:
        if c in ")]}>":
            score += {")": 3, "]": 57, "}": 1197, ">": 25137}[c]
            break
    max_score = max(max_score, score)

# Print the maximum syntax error score
print(max_score)
""""""