"""Here is a solution to the problem in Python. This solution uses a stack to keep track of the open characters, and updates the score accordingly if an illegal character is found.

"""
score = 0
stack = []

# Open the input file
with open("10_input", "r") as f:
    # Read each line of the input
    for line in f:
        # Keep track of whether the line is corrupted
        corrupted = False
        # Loop through each character in the line
        for c in line:
            # If the character is an open character, push it onto the stack
            if c in ["(", "[", "{", "<"]:
                stack.append(c)
            # If the character is a closing character
            elif c in [")", "]", "}", ">"]:
                # Check if the stack is empty
                if len(stack) == 0:
                    # If the stack is empty, the line is corrupted
                    corrupted = True
                    break
                # Get the top character on the stack
                top = stack.pop()
                # Check if the top character on the stack matches the closing character
                if (top, c) not in [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]:
                    # If the characters do not match, the line is corrupted
                    corrupted = True
                    break
        # Check if the stack is not empty at the end of the line
        if len(stack) != 0:
            # If the stack is not empty, the line is corrupted
            corrupted = True
        # If the line is corrupted, update the score
        if corrupted:
            # Get the first illegal character on the line
            illegal = c
            # Update the score based on the illegal character
            if illegal == ")":
                score += 3
            elif illegal == "]":
                score += 57
            elif illegal == "}":
                score += 1197
            elif illegal == ">":
                score += 25137

# Print the final score
print(score)
""""""