"""To solve this problem, we can read the input from the `10_input` file, line by line. For each line, we can iterate through the characters in the line and check if the current character is a opening bracket or closing bracket. If it's a opening bracket, we can push it to a stack, and if it's a closing bracket, we can pop the last opening bracket from the stack. If the popped opening bracket is not a valid pair for the closing bracket, we can stop iterating through the line and add the corresponding score for the closing bracket to the total score.

Here is an implementation of the solution in Python:

"""
# Read input from file
with open('10_input', 'r') as f:
    lines = f.readlines()

# Dictionary of scores for each closing bracket
scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# Initialize total score
total_score = 0

# Iterate through each line
for line in lines:
    # Initialize stack
    stack = []
    
    # Iterate through characters in line
    for ch in line:
        # If character is opening bracket, push it to stack
        if ch in ('(', '[', '{', '<'):
            stack.append(ch)
        # If character is closing bracket
        elif ch in (')', ']', '}', '>'):
            # If stack is empty or the last opening bracket is not a valid pair for the closing bracket, add score and stop iterating
            if not stack or (stack.pop() + ch) not in ('()', '[]', '{}', '<>'):
                total_score += scores[ch]
                break

# Print total score
print(total_score)
""""""