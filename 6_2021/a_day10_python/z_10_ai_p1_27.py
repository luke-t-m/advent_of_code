"""You can solve this problem by using a stack to track the opening and closing brackets in the navigation subsystem. 

First, create an empty stack and a dictionary with the possible bracket pairs. Then, read the input from the file line by line and iterate over each character in the line. If the character is an opening bracket, push it onto the stack. If it is a closing bracket, pop the last opening bracket from the stack and check if the pair is valid according to the dictionary. If the pair is not valid, the line is corrupted and you can stop processing the line and move on to the next one.

At the end, you can print the total score for all the corrupted lines by adding up the scores for the first illegal character on each line. Here is some sample code that illustrates how you could solve this problem:

"""
# Create a dictionary with the possible bracket pairs
bracket_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

# Initialize the total score to 0
total_score = 0

# Open the input file
with open('10_input') as f:
    # Read each line from the file
    for line in f:
        # Initialize an empty stack for this line
        stack = []

        # Iterate over each character in the line
        for c in line:
            # If the character is an opening bracket, push it onto the stack
            if c in bracket_pairs:
                stack.append(c)
            # If the character is a closing bracket, pop the last opening bracket
            # from the stack and check if the pair is valid
            elif c in bracket_pairs.values():
                if stack and bracket_pairs[stack[-1]] == c:
                    stack.pop()
                else:
                    # The line is corrupted, so add the score for the first
                    # illegal character to the total score
                    total_score += {
                        ')': 3,
                        ']': 57,
                        '}': 1197,
                        '>': 25137
                    }[c]
                    break

# Print the total score for all the corrupted lines
print(total_score)
""""""