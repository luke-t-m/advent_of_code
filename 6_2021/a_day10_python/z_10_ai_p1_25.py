# Read input from file called 10_input
with open('10_input') as f:
    input = f.read()

# Split input into lines and remove corrupted lines
lines = input.strip().split('\n')
lines = [line for line in lines if not any(ch in line for ch in [')', ']', '}', '>'])]

# Calculate the score for each remaining line
score = 0
for line in lines:
    # Keep track of which chunks are open
    stack = []
    for ch in line:
        # If the character opens a new chunk, add it to the stack
        if ch in ['(', '[', '{', '<']:
            stack.append(ch)
        # Otherwise, check if the character closes the current chunk
        elif ch in [')', ']', '}', '>']:
            if len(stack) == 0:
                break
            elif ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            elif ch == '>' and stack[-1] == '<':
                stack.pop()
    # If the stack is empty, the line is correct and we can add the score
    if len(stack) == 0:
        score += len(line)

# Print the final score
print(score)