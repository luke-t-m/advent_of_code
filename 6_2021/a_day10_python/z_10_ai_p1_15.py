"""The problem can be solved by iterating through each character in the input string, and keeping track of the open brackets. If we encounter a closing bracket, we check if it matches the most recent open bracket. If it does not, we stop parsing that line and add the corresponding score to the total score.

Here is one way to solve the problem in Python:

"""
score = 0

# Dictionary mapping closing bracket to score
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

# Stack to keep track of open brackets
stack = []

with open("10_input") as f:
    for line in f:
        # Parse the line character by character
        for c in line:
            if c in ["(", "[", "{", "<"]:
                # If we encounter an open bracket, push it onto the stack
                stack.append(c)
            elif c in scores:
                # If we encounter a closing bracket, check if it matches the most recent open bracket
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    # If the bracket does not match, add the corresponding score to the total score
                    score += scores[c]
                    # Stop parsing the line
                    break

# Print the final score
print(score)
""""""