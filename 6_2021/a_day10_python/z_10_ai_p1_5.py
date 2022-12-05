"""To solve this problem in python, you can use a stack data structure to keep track of the opening characters. You can iterate over the characters in the input string and add the opening characters to the stack. When you encounter a closing character, you can check if it matches the top element on the stack. If it does, you can pop the top element off the stack. Otherwise, you can stop processing the line and print the score of the illegal character. Here is an example solution:

"""
# Read the input from the file 10_input
with open('10_input', 'r') as f:
    input_str = f.read()

# Create a mapping of characters to scores
score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}

# Initialize the stack and score
stack = []
score = 0

# Iterate over the characters in the input string
for c in input_str:
    # If the character is an opening character, add it to the stack
    if c in ('(', '[', '{', '<'):
        stack.append(c)
    # If the character is a closing character, check if it matches the top
    # element on the stack. If it does, pop the top element off the stack.
    # Otherwise, stop processing the line and print the score of the illegal
    # character.
    elif c in (')', ']', '}', '>'):
        if stack and stack[-1] == c:
            stack.pop()
        else:
            score += score_map[c]
            break

# Print the final score
print(score)
""""""