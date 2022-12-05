"""Here is a solution in Python:

"""
# Read the input from a file called 10_input
with open("10_input", "r") as f:
    lines = f.read().strip().split("\n")

# Define a dictionary that maps the closing characters to their corresponding scores
score_table = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

# Initialize the total score to 0
total_score = 0

# Loop over all the lines in the input
for line in lines:

    # Initialize the score for the current line to 0
    line_score = 0

    # Initialize a stack to keep track of the open characters we encounter
    stack = []

    # Loop over all the characters in the line
    for c in line:

        # If the character is an opening character, add it to the stack
        if c in ("(", "[", "{", "<"):
            stack.append(c)

        # If the character is a closing character, check if it matches the
        # corresponding opening character
        elif c in (")", "]", "}", ">"):
            if not stack or c != {"(": ")", "[": "]", "{": "}", "<": ">"}[stack[-1]]:
                line_score += score_table[c]
                break
            else:
                stack.pop()

    # If the stack is empty, add the score for the current line to the total score
    if not stack:
        total_score += line_score

# Print the total score
print(total_score)
""""""