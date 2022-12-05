"""To solve this problem, we will write a python script that reads the input file and processes each line, scoring the syntax error in the line and ignoring corrupted lines. Here is one way to do this:

"""
# Read the input from the file "10_input"
with open("10_input", "r") as input_file:
    lines = input_file.readlines()

# Define a dictionary that maps illegal closing characters to their scores
SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}

# Initialize the total score to 0
total_score = 0

# Loop over each line in the input
for line in lines:
    # Initialize a stack to keep track of open brackets
    stack = []

    # Loop over each character in the line
    for ch in line:
        # If the character is an opening bracket, push it onto the stack
        if ch in ["(", "[", "{", "<"]:
            stack.append(ch)
        # If the character is a closing bracket, pop the last opening bracket from the stack
        elif ch in [")", "]", "}", ">"]:
            # If the stack is empty or the last opening bracket doesn't match the current closing bracket,
            # the line is corrupted and we should stop processing it
            if not stack or (ch == ")" and stack[-1] != "(") or (ch == "]" and stack[-1] != "[") or (ch == "}" and stack[-1] != "{") or (ch == ">" and stack[-1] != "<"):
                break
            # Otherwise, pop the last opening bracket from the stack and add the score of the current closing bracket
            # to the total score
            else:
                stack.pop()
                total_score += SCORES[ch]

    # If the stack is not empty at the end of the line, the line is corrupted
    if stack:
        continue

# Print the total score
print(total_score)
""""""